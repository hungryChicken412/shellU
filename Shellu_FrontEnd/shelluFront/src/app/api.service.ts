import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http:HttpClient) { }

  baseUrl = "http://localhost:8000"
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

  getAllPuzzles(): Observable<any>{
    return this.http.get(this.baseUrl + '/puzzles/', {headers: this.httpHeaders})
  }

  getSinglePuzzle(puzzle: string){
    return this.http.get(this.baseUrl + '/puzzles/'+puzzle, {headers: this.httpHeaders})
  }
}
