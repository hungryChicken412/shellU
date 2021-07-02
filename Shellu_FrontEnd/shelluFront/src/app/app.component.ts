import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService],
})

export class AppComponent {
  title = 'shelluFront';
  categories = [{puzzle_category:'easy'},{puzzle_category:'hard'}]

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

   
}
