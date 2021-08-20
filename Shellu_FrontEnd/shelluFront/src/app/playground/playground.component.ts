import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';
import { Router  } from '@angular/router';
import {switchMap} from 'rxjs/operators';


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

  constructor(private api:ApiService, private router:Router) {

   }

   getPuzzle(name: string){
    this.api.getSinglePuzzle(name).subscribe(
      data => {
        this.q = data[0];

      },
      error => {
        alert(error);
      }
    )
  }


  ngOnInit(): void {
    const url = this.router.url;
    const wurl = url.split('/')[2];
    
    this.getPuzzle(wurl);
    console.log('loading', wurl);

    
  }

  

}
