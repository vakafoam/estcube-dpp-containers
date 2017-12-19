import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { PlatformComponent } from './platform/platform.component';
import { SpinnerComponent } from './platform/spinner/spinner.component';

import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule ],
    declarations: [
        AppComponent,
        PlatformComponent,
        SpinnerComponent
       ],
    bootstrap: [ AppComponent ]
})

export class AppModule {}
