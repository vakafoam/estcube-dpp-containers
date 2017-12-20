import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

import { PLATFORM } from '../shared/constant/constants';
import { URLS } from '../shared/constant/constants';

import { UploadService } from './service/upload.service';

@Component({
    moduleId: module.id,
    selector: 'platform',
    templateUrl: 'platform.component.html',
    styleUrls: ['platform.component.css'],
    providers: [UploadService]
})

export class PlatformComponent implements OnInit {
    private platforms = PLATFORM;
    private platformArr: string[] = [];
    private platForm: FormGroup;
    private selectedPlatform: string;
    private scriptFile: File;
    private result;
    private resultReceived: boolean = false;
    public loader: boolean = false;
    public error: string;


    constructor(private formB: FormBuilder, private service: UploadService) { }

    ngOnInit() {
        this.platformArr = Object.keys(this.platforms).filter(Number);
        this.configureForm();
    }

    configureForm() {
        this.platForm = this.formB.group({
            platform: [1, Validators.required]
        });
    }

    submitSelected() {
        this.selectedPlatform = this.platforms[this.platForm.value["platform"]];
        console.log("Selected Platform: " + this.selectedPlatform);
    }

    getURL(): string {
        return URLS[this.selectedPlatform];
    }

    fileChange(event) {
      this.error = null;
        this.scriptFile = event.target.files[0];
        console.log("file chosen");
        console.log(this.scriptFile.name);
    }

    upload() {
        this.resultReceived = false;
        this.submitSelected();
        this.loader = true;

        console.log('Url: '+this.getURL());
        this.service.makeFileRequest(this.getURL(), [], this.scriptFile) // to flask broker
            .subscribe((res) => {
                console.log("Result: ", res);
                this.result = res;
                this.resultReceived = true;
                this.loader = false;
            }, (error) => {
                this.loader = false;
                if (!error) {
                  this.error = "! Server Error ! File format is not supported";
                } else {
                  this.error = "! Server Error ! " + error;
                }
                console.error("ERROR: ", error);
            });
    }

    imageFromResult(): string {
        let encodedImage = null;
        if (this.resultReceived && this.result['image'].toString() != '[object Object]') {
          encodedImage = this.result['image'];
          console.log("Encoded image: ", encodedImage.toString());
        }
        return encodedImage;
    }

}
