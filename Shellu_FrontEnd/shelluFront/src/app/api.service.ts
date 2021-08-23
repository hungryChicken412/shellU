import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http:HttpClient, private router: Router) { }

  baseUrl = "http://localhost:8000";
  token = localStorage.getItem('token');
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization' : 'token ' + this.token});
  
  executionHeaders = new HttpHeaders({
    'Content-Type': 'application/json',
    'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
    'x-rapidapi-key': "6d7fc6a905msh8b2442bfb68098bp13a19fjsn444337cba7d8"
  });

  codexURL = "https://codexweb.netlify.app/.netlify/functions/enforceCode";

  getAllPuzzles(): Observable<any>{
    if(typeof this.token === 'undefined' || this.token === null || this.token === 'undefined'){
      this.router.navigate(['login']);
    }
    return this.http.get(this.baseUrl + '/api/puzzles/', {headers: this.httpHeaders})
  }

  getSinglePuzzle(puzzle: any): Observable<any> {
    /*if(typeof this.token === 'undefined' || this.token === null || this.token === 'undefined'){
      this.router.navigate(['login']);
    }
    */
    return this.http.get(this.baseUrl + '/api/puzzle/' + puzzle + '/' , {headers: this.httpHeaders})
  }

  loginUser(userData: any): Observable<any> {
    return this.http.post(this.baseUrl + '/auth/', userData);
  }

  getUser(username:string): Observable<any>{
    if(typeof this.token === 'undefined' || this.token === null || this.token === 'undefined'){
      this.router.navigate(['login']);
    }
    return this.http.get(this.baseUrl + '/api/users/' + username + '/', {headers: this.httpHeaders})
  }

  puzzleSubmit(puzzleSlug : string): Observable<any> {
    if(typeof this.token === 'undefined' || this.token === null || this.token === 'undefined'){
      this.router.navigate(['login']);
    }
    return this.http.get(this.baseUrl + '/api/solved/' + puzzleSlug + '/', {headers: this.httpHeaders})
  }
  

}
