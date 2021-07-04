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
  
  q: any;

  constructor(private api:ApiService, private router:Router) {

   }

   getPuzzle(name: string){
    this.api.getSinglePuzzle(name).subscribe(
      data => {
        const puzzle = data;
        this.q = puzzle;
      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {
    const url = this.router.url;
    const wurl = url.split('/')[2];
    
    this.getPuzzle(wurl);
    console.log(wurl);

    
  }

}
