import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';

@Component({
  selector: 'app-puzzle-list',
  templateUrl: './puzzle-list.component.html',
  styleUrls: ['./puzzle-list.component.css'],
  providers: [ApiService],
})
export class PuzzleListComponent implements OnInit {

  puzzles = [{puzzle_category:'easy'},{puzzle_category:'hard'}]

  constructor(private api:ApiService) { 
    this.getCats();
  }

   getCats = () => {
     this.api.getAllCats().subscribe(
       data => {
         this.categories = data
       },
       error => {
         console.log(error)
       }
     )
   }

  ngOnInit(): void {
  }

}
