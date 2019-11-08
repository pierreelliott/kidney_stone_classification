import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ClasseCalculComponent } from './classe-calcul.component';

describe('ClasseCalculComponent', () => {
  let component: ClasseCalculComponent;
  let fixture: ComponentFixture<ClasseCalculComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ClasseCalculComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ClasseCalculComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
