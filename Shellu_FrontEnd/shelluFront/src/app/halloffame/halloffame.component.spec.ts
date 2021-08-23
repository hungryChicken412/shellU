import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HalloffameComponent } from './halloffame.component';

describe('HalloffameComponent', () => {
  let component: HalloffameComponent;
  let fixture: ComponentFixture<HalloffameComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HalloffameComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HalloffameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
