import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';
@Component({
  selector: 'app-halloffame',
  templateUrl: './halloffame.component.html',
  styleUrls: ['./halloffame.component.css']
})
export class HalloffameComponent implements OnInit {
  data:any;

  constructor(private api:ApiService) {this.getHighscores(); }
  
  getHighscores = () => {
    this.api.getScores().subscribe(
      data => {
        this.data = data;
        for (let index = 0; index < this.data.length; index++) {
          const level = this.data[index].level;

          if (level == 0){
          this.data[index].level = "Sleepy-Baby"
          }
          else if (level == 1){
            this.data[index].level = "Basic-Teen"
          }
          else if (level == 2){
            this.data[index].level = "Average-Nerd"
          }
          else if (level == 3){
            this.data[index].level = "Script-Kiddie"
          }
          else if (level == 4 ){
            this.data[index].level = "Master"
          }
          else if (level == 5){
            this.data[index].level = "Hacker"
          }
          
        }
        console.log(this.data)    
      },
      error => {
        console.log(error)
      }
    )
  }
  ngOnInit(): void {
  }

}
