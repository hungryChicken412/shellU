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
import { Router } from '@angular/router';

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
    {level: '0'},
    {puzzles_completed: 0},
    {username: "popdopqoplop"},

  ]

  constructor(private api:ApiService, private router: Router) { this.getUserData() }

  getUserData = () => {
    this.api.getUser('me').subscribe(
      data => {
        this.userdata = data;
        var level = this.userdata[0].level;
        if (level == '0'){
          this.userdata[0].level = "Sleepy Baby"
          }
          else if (level == '1'){
            this.userdata[0].level = "Basic Teen"
          }
          else if (level == '2'){
            this.userdata[0].level = "Average Nerd"
          }
          else if (level == '3'){
            this.userdata[0].level = "Script Kiddie"
          }
          else if (level == '4' ){
            this.userdata[0].level = "Master"
          }
          else if (level == '5'){
            this.userdata[0].level = "Hacker"
          }  
      },
      error => {
        console.log(error)
      }
    )
  }

  editUserData(){
    this.api.editUser(this.userdata[0].info, this.userdata[0].languages).subscribe(
      data => {
        window.location.reload();
      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {
  }

}
