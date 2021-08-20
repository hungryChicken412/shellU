import { Component, OnInit } from '@angular/core';
import {
  trigger,
  state,
  style,
  animate,
  transition,
  // ...
} from '@angular/animations';
import { ApiService } from '.././api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  animations: [
    // animation triggers go here
  ],
  providers: [ApiService],
})



export class HomeComponent implements OnInit {

  userdata = [
    {XP: 0},
    {avatar: "http://localhost:8000/media/chicken.jpg"},
    {courses_completed: 0},
    {global_rank: 0},
    {info: ''},
    {languages: "N\\A"},
    {level: 0},
    {puzzles_completed: 0},
    {username: "popdopqoplop"},

  ]

  constructor(private api:ApiService) { this.getUserData() }

  getUserData = () => {
    this.api.getUser('me').subscribe(
      data => {
        this.userdata = data;  
        console.log(this.userdata)    
      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {
  }

}
