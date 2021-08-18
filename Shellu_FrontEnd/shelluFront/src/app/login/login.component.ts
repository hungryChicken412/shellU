import { Component, OnInit } from '@angular/core';
import { ApiService } from '.././api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [ApiService],
})
export class LoginComponent implements OnInit {
  input = {
    username: '',
    password: ''
  };

  constructor(private api:ApiService, private router: Router) { 

  }

  ngOnInit(): void {
    this.input = {
      username: '',
      password: ''
    }
  }

  onLogin () {
    this.api.loginUser(this.input).subscribe(
      response => {
        localStorage.setItem('token', response.token);
        this.router.navigate(['challenges']);
      },
      error => {
        console.log('error', error);
      }
    )
  }

  



}
