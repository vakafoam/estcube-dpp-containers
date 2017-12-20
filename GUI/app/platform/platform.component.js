"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var forms_1 = require('@angular/forms');
var constants_1 = require('../shared/constant/constants');
var constants_2 = require('../shared/constant/constants');
var upload_service_1 = require('./service/upload.service');
var PlatformComponent = (function () {
    function PlatformComponent(formB, service) {
        this.formB = formB;
        this.service = service;
        this.platforms = constants_1.PLATFORM;
        this.platformArr = [];
        this.resultReceived = false;
        this.loader = false;
    }
    PlatformComponent.prototype.ngOnInit = function () {
        this.platformArr = Object.keys(this.platforms).filter(Number);
        this.configureForm();
    };
    PlatformComponent.prototype.configureForm = function () {
        this.platForm = this.formB.group({
            platform: [1, forms_1.Validators.required]
        });
    };
    PlatformComponent.prototype.submitSelected = function () {
        this.selectedPlatform = this.platforms[this.platForm.value["platform"]];
        console.log("Selected Platform: " + this.selectedPlatform);
    };
    PlatformComponent.prototype.getURL = function () {
        return constants_2.URLS[this.selectedPlatform];
    };
    PlatformComponent.prototype.fileChange = function (event) {
        this.error = null;
        this.scriptFile = event.target.files[0];
        console.log("file chosen");
        console.log(this.scriptFile.name);
    };
    PlatformComponent.prototype.upload = function () {
        var _this = this;
        this.resultReceived = false;
        this.submitSelected();
        this.loader = true;
        console.log('Url: ' + this.getURL());
        this.service.makeFileRequest(this.getURL(), [], this.scriptFile) // to flask broker
            .subscribe(function (res) {
            console.log("Result: ", res);
            _this.result = res;
            _this.resultReceived = true;
            _this.loader = false;
        }, function (error) {
            _this.loader = false;
            if (!error) {
                _this.error = "! Server Error ! File format is not supported";
            }
            else {
                _this.error = "! Server Error ! " + error;
            }
            console.error("ERROR: ", error);
        });
    };
    PlatformComponent.prototype.imageFromResult = function () {
        var encodedImage = null;
        if (this.resultReceived && this.result['image'].toString() != '[object Object]') {
            encodedImage = this.result['image'];
            console.log("Encoded image: ", encodedImage.toString());
        }
        return encodedImage;
    };
    PlatformComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'platform',
            templateUrl: 'platform.component.html',
            styleUrls: ['platform.component.css'],
            providers: [upload_service_1.UploadService]
        }), 
        __metadata('design:paramtypes', [forms_1.FormBuilder, upload_service_1.UploadService])
    ], PlatformComponent);
    return PlatformComponent;
}());
exports.PlatformComponent = PlatformComponent;
//# sourceMappingURL=platform.component.js.map