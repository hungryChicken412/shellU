import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';
import { Router  } from '@angular/router';
import {switchMap} from 'rxjs/operators';
/* eslint-disable */
// @ts-ignore
import { piston } from 'piston-client';
import { NgZone } from '@angular/core';
import { DOCUMENT } from '@angular/common';
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
    "puzzle_slug": '1',
    "content": "<p>aqweqweqwe</p>",
    "puzzleDesiredOutput" : "",
    "functionName": "0",
    "puzzleSolution": "",
    "hint": "",
    "starterCode": "",
    "testCases" : "",
    "xps": 0,
    "hasDone" : true,
  };
  nextPuzzleLink = "";

  code = "";
  language = "python";
  input ="";
  output = "#Your code's output will appear here!";
  constructor(private api:ApiService, private router:Router, private ngZone: NgZone )  {

   }

   getPuzzle(name: string){
    this.api.getSinglePuzzle(name).subscribe(
      data => {
        this.q = data[0];
        this.code = this.q.starterCode;
        var slug = parseInt(this.q.puzzle_slug) + 1 ;
        this.nextPuzzleLink = '/playground/'+slug.toString();
        if (this.q.hasDone){
          this.q.title += " - [COMPLETED]";
          
        }
        console.log(this.nextPuzzleLink);

      },
      error => {
        /*alert(error);*/
      }
    )
  }

  executeCode(){
    
    this.output = "##Evaluating!";
    var finalExcecutionCMD1;
    var finalExcecutionCMD2;
    
    var lines = this.q.testCases.split('|');
    console.log(lines)
    var aa1 = lines[1].split(':');
    console.log(aa1)
    var bb1 = lines[2].split(':');
    
    if (this.language.valueOf() == "python"){
    finalExcecutionCMD1 = this.code + '\n\n' + "print(" + this.q.functionName + '(' + aa1[0].trim() + '))';
    finalExcecutionCMD2 = this.code + '\n\n' + "print(" + this.q.functionName + '(' + bb1[0].trim() + '))';
    } else if (this.language.valueOf() == "javascript"){
      finalExcecutionCMD1 = this.code + '\n\n' + "console.log(" + this.q.functionName + '(' + aa1[0].trim() + '))';
      finalExcecutionCMD2 = this.code + '\n\n' + "console.log(" + this.q.functionName + '(' + bb1[0].trim() + '))';
    }
    
    

    
    (async () => {
      
      const client = piston({ server: "https://emkc.org" });
      
      const runtimes = await client.runtimes();
      // [{ language: 'python', version: '3.9.4', aliases: ['py'] }, ...]
  
      const result1 = await client.execute(this.language, finalExcecutionCMD1);
      this.output = result1.run.output;
      if (this.output.trim().valueOf() === this.q.puzzleDesiredOutput.trim().valueOf()){
        const result2 = await client.execute(this.language, finalExcecutionCMD2);
        this.output += '\n' + result2.run.output;
        if (result2.run.output.trim().valueOf() == bb1[1].trim().valueOf()){
          this.output += '\n' + "! Congratulations! You Passed !";
          this.submitPuzzle(this.q.puzzle_slug);
        } else {
          this.output += '\n' + "[ERROR]: Second test failed!";
        }
      } else {
        this.output += '\n' + "[ERROR]: First test failed!";
      }
      
      
      
      
  
  })();
    
  }

  submitPuzzle(slug:string){
    this.api.puzzleSubmit(slug).subscribe(
      data => {
        /**/
        (<HTMLInputElement>document.getElementById("congratsBanner")).style.display = "flex";
        

      },
      error => {
        /*alert(error);*/
      }
    )
  }
  
  ngOnInit(): void {
    const url = this.router.url;
    const wurl = url.split('/')[2];
    
    this.getPuzzle(wurl);
    
    

    
  }

  

}
