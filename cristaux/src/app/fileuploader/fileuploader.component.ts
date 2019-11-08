import { Component, Input, OnInit } from '@angular/core';
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';

const URL_classe = 'http://localhost:8000/classification_cristaux/classerCristal/SEC';
const URL_upload = 'http://localhots:8000/classification_cristaux/chargerCristal';

@Component({
  selector: 'app-fileuploader',
  templateUrl: './fileuploader.component.html',
  styleUrls: ['./fileuploader.component.css']
})
export class FileuploaderComponent implements OnInit {
    @Input() typeOfUpload: String;

    public url2; edited; response; gottenResponse; URL; button;
    public username; password; typeImage; classeCalcul;

    constructor() {
        this.url2 = '';
        this.edited = false;
        this.gottenResponse = true;
        this.response = '';
        this.URL = '';
        this.button = '';
        this.username = '';
        this.password = '';
        this.typeImage = 'SEC';
        this.classeCalcul = 'Ia';
        this.typeOfUpload = 'upload';
    }

    public uploader: FileUploader = new FileUploader({url: URL_upload, itemAlias: 'image'});

    ngOnInit() {
        if (this.typeOfUpload === 'upload') {
            this.URL = URL_upload;
            this.button = 'Envoyer l\'image';
        } else {
            this.URL = URL_classe;
            this.button = 'Classer l\'image';
        }

        this.uploader = new FileUploader({url: this.URL, itemAlias: 'image'});

        this.uploader.onAfterAddingFile = (file) => {
            file.withCredentials = false;
        };
        this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
            console.log(response.toString());
            console.log('ImageUpload:uploaded:', item, status, response);
            alert(response.toString());
            location.reload();
            document.getElementById('classe').style.display = 'block';
            this.response = response;
            return response;
        };
        this.uploader.onBuildItemForm = (fileItem: any, form: any) => {
            form.append('username', this.username);
            form.append('password', this.password);
            form.append('classe', this.classeCalcul);
            form.append('type', this.typeImage);
        };

    }

    readUrl(event: any) {
        console.log('readUrl');
        console.log(event);
        if (event.target.files && event.target.files[0]) {
          console.log('event');
            const reader = new FileReader();

            console.log(reader.onload);

            reader.onload = (event1: any) => {
                this.url2 = event1.target.result;
                this.edited = true;
            }

            reader.readAsDataURL(event.target.files[0]);
        }
    }
}
