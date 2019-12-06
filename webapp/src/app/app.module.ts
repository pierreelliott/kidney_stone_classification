import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FileSelectDirective } from 'ng2-file-upload';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { UploaderComponent } from './uploader/uploader.component';
import { FileuploaderComponent } from './fileuploader/fileuploader.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { ClasseCalculComponent } from './classe-calcul/classe-calcul.component';
import { UploadCalculComponent } from './upload-calcul/upload-calcul.component';
import { HeaderComponent } from './header/header.component';
import { AboutitComponent } from './aboutit/aboutit.component';
import { FooterComponent } from './footer/footer.component';
//import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    UploaderComponent,
    FileSelectDirective,
    FileuploaderComponent,
    PageNotFoundComponent,
    ClasseCalculComponent,
    UploadCalculComponent,
    HeaderComponent,
    AboutitComponent,
    FooterComponent,
   // FontAwesomeModule
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
