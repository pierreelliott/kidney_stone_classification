import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadCalculComponent } from './upload-calcul.component';

describe('UploadCalculComponent', () => {
  let component: UploadCalculComponent;
  let fixture: ComponentFixture<UploadCalculComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UploadCalculComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadCalculComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
