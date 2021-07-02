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

  getAllCats(): Observable<any>{
    return this.http.get(this.baseUrl + '/category/', {headers: this.httpHeaders})
  }
}
