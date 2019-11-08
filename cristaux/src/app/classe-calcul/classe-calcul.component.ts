import { Component, Input, OnInit } from '@angular/core';
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';


const URL_classe = 'http://calculs.clement-cottet.fr/classification_cristaux/classerCristal/';
const URL_upload = 'http://calculs.clement-cottet.fr/classification_cristaux/chargerCristal';


@Component({
  selector: 'app-classe-calcul',
  templateUrl: './classe-calcul.component.html',
  styleUrls: ['./classe-calcul.component.css']
})
export class ClasseCalculComponent implements OnInit {

    @Input() typeOfUpload: String;

    public url1; edited; response; gottenResponse; URL; button;
    public username; password; typeImage; classeCalcul;


    constructor() {
        this.url1 = '';
        this.edited = false;
        this.gottenResponse = true;
        this.response = '';
        this.URL = '';
        this.button = '';
        this.username = '';
        this.password = '';
        this.typeImage = 'SEC';
        this.classeCalcul = 'Ia';
    }


    public uploader: FileUploader = new FileUploader({url: URL_classe, itemAlias: 'image'});

    ngOnInit() {
        if (this.typeOfUpload === 'upload') {
            this.URL = URL_upload;
            this.button = 'Envoyer l\'image';
        } else {
            this.URL = URL_classe + this.typeImage;
            this.button = 'Classer l\'image';
        }

        this.uploader = new FileUploader({url: this.URL, itemAlias: 'image'});

        this.uploader.onAfterAddingFile = (file) => {
            file.withCredentials = false;
        };
        this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
            if(response.toString() == 'Autre'){
                document.getElementById('resultat').innerText = "Notre algorithme ne peut pas classifier cette image, "+
                    "soit c'est un calcul peu répendu, soit vous essayez de le berner!";
            }
            else{
              if(this.typeImage === 'SEC'){
                document.getElementById('resultat').innerText = "Notre agorithme pense que ce calcul est une section de classe " + response.toString() ;
              } else{
                document.getElementById('resultat').innerText = "Notre agorithme pense que ce calcul est une surface de classe " + response.toString() ;
              }
            }
            //console.log(response.toString());
            //console.log('ImageUpload:uploaded:', item, status, response);
            document.getElementById('classe').style.display = 'block';
            this.response = response;
            return response;
        };
        if (this.typeOfUpload === 'upload') {
            this.uploader.onBuildItemForm = (fileItem: any, form: any) => {
                form.append('username', this.username);
                form.append('password', this.password);
                form.append('classe', this.classeCalcul);
                form.append('type', this.typeImage);
            };
        }
    }

    readUrl(event: any) {
        console.log('readUrl');
        if (event.target.files && event.target.files[0]) {
            const reader = new FileReader();

            reader.onload = (event1: any) => {
                this.url1 = event1.target.result;
                this.edited = true;
            }

            reader.readAsDataURL(event.target.files[0]);
            console.log(event.target.files[0]);
        }
    }

    reset(){
      if (this.typeOfUpload === 'upload') {
        this.URL = URL_upload;
        this.button = 'Envoyer l\'image';
      } else {
        this.URL = URL_classe + this.typeImage;
        this.button = 'Classer l\'image';
      }

      this.uploader = new FileUploader({url: this.URL, itemAlias: 'image'});

      this.uploader.onAfterAddingFile = (file) => {
        file.withCredentials = false;
      };
      this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
        if(response.toString() == 'Autre'){
          document.getElementById('resultat').innerText = "Notre algorithme ne peut pas classifier cette image, "+
            "soit c'est un calcul peu répendu, soit vous essayez de le berner!";
        }
        else{
          if(this.typeImage === 'SEC'){
            document.getElementById('resultat').innerText = "Notre agorithme pense que ce calcul est une section de classe " + response.toString() ;
          } else{
            document.getElementById('resultat').innerText = "Notre agorithme pense que ce calcul est une surface de classe " + response.toString() ;
          }
        }
        //console.log(response.toString());
        //console.log('ImageUpload:uploaded:', item, status, response);
        //alert('File uploaded successfully');
        document.getElementById('classe').style.display = 'block';
        this.response = response;
        return response;
      };
    }

}
