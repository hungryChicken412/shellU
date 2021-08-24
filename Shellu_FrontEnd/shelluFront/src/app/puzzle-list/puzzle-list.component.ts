import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';

@Component({
  selector: 'app-puzzle-list',
  templateUrl: './puzzle-list.component.html',
  styleUrls: ['./puzzle-list.component.css'],
  providers: [ApiService],
})
export class PuzzleListComponent implements OnInit {

  puzzles = [{title:'easy'},{puzzle_category:'hard'}, {puzzle_slug: 'slug'}, {content: 'content'}, {answer: 'answer'}, {xps:'0'}]

  constructor(private api:ApiService) { 
    this.getPuzzles();
  }

  getPuzzles = () => {
     this.api.getAllPuzzles().subscribe(
       data => {
         this.puzzles = data;
         console.log("let me tell you something");
         for (let index = 0; index < this.puzzles.length; index++) {
           const element = this.puzzles[index];
           if (this.puzzles[index].puzzle_category == "http://localhost:8000/api/category/1/"){
            this.puzzles[index].puzzle_category = 'Easy'
           } else if (this.puzzles[index].puzzle_category == "http://localhost:8000/api/category/2/"){
            this.puzzles[index].puzzle_category = 'Medium'
           }else if (this.puzzles[index].puzzle_category == "http://localhost:8000/api/category/3/"){
            this.puzzles[index].puzzle_category = 'Hard'
           }
           
         }

       },
       error => {
         console.log(error)
       }
     )
   }

  ngOnInit(): void {
  }

}
