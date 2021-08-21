import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';
import { Router  } from '@angular/router';
import {switchMap} from 'rxjs/operators';
/* eslint-disable */
// @ts-ignore
import { piston } from 'piston-client';
import { NgZone } from '@angular/core';
/* eslint-enable */

@Component({
  selector: 'app-playground',
  templateUrl: './playground.component.html',
  styleUrls: ['./playground.component.css'],
  providers: [ApiService],
})
export class PlaygroundComponent implements OnInit {
  
  q = {
    "title": "Help me",
    "puzzle_category": "http://localhost:8000/api/category/1/",
    "puzzle_slug": "1",
    "content": "<p>aqweqweqwe</p>",
    "answer": "0",
    "puzzleSolution": "",
    "hint": "",
    "starterCode": "",
    "testCases": "",
    "xps": 0
  };

  code = "";
  language = "python";
  input ="";
  output = "#Your code's output will appear here!";

  count = 0
  

  constructor(private api:ApiService, private router:Router, private ngZone: NgZone )  {

   }

   getPuzzle(name: string){
    this.api.getSinglePuzzle(name).subscribe(
      data => {
        this.q = data[0];

      },
      error => {
        /*alert(error);*/
      }
    )
  }

  executeCode(){
    
    this.output = "##Evaluating!";
    (async () => {
      
      const client = piston({ server: "https://emkc.org" });
      
      const runtimes = await client.runtimes();
      // [{ language: 'python', version: '3.9.4', aliases: ['py'] }, ...]
  
      const result = await client.execute(this.language, this.code);
      // { language: 'python', version: '3.9.4', run: {
      //     stdout: 'Hello World!\n',
      //     stderr: '',
      //     code: 0,
      //     signal: null,
      //     output: 'Hello World!\n'
      // }}
      
      this.output = result.run.output;
      
      
  
  })();
  
  }

  plusOne(){
    this.count += 1;
  }

  changeCounter(codeOutput: string):void{
    this.output = codeOutput;
  }


  ngOnInit(): void {
    const url = this.router.url;
    const wurl = url.split('/')[2];
    
    this.getPuzzle(wurl);
    console.log('loading', wurl);

    
  }

  

}
