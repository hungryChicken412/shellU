import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PlaygroundComponent } from './playground/playground.component';
import { PuzzleListComponent } from './puzzle-list/puzzle-list.component';

const routes: Routes = [
  { path:'', component: HomeComponent },
  { path:'playground', component: PlaygroundComponent },
  { path: 'challenges', component:PuzzleListComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
