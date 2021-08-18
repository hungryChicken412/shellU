import { Component } from '@angular/core';
import { ApiService } from './api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService],
})

export class AppComponent {
  title = 'shelluFront';


  constructor(private api:ApiService, private router: Router) { 

   }

   logOut(){
    localStorage.removeItem('token');
    this.router.navigate(['login']);
   }

   
}
