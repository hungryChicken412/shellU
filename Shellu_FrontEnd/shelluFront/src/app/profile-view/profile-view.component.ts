import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-profile-view',
  templateUrl: './profile-view.component.html',
  styleUrls: ['./profile-view.component.css']
})
export class ProfileViewComponent implements OnInit {
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

  constructor(private api:ApiService, private router:Router) { }
  getUserData = (name:string) => {
    this.api.getUser(name).subscribe(
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
        console.log(this.userdata)    
      },
      error => {
        console.log(error)
      }
    )
  }
  ngOnInit(): void {
    const url = this.router.url;
    const wurl = url.split('/')[2];
    
    
    this.getUserData(wurl);
  }

}
