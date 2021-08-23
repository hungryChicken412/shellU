import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HalloffameComponent } from './halloffame/halloffame.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { NotfoundComponent } from './notfound/notfound.component';
import { PlaygroundComponent } from './playground/playground.component';
import { PuzzleListComponent } from './puzzle-list/puzzle-list.component';

const routes: Routes = [


  { path:'', component: HomeComponent },
  { path:'playground', component: PlaygroundComponent,
    children: [
      { path: ':name', component:PlaygroundComponent }
    ]},
    
  { path: 'challenges', component:PuzzleListComponent,
    children: [
      { path:':name', redirectTo: '/playground/:name'},
    ]},
  { path:'login', component: LoginComponent },
  { path:'scoreboard', component: HalloffameComponent },


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
