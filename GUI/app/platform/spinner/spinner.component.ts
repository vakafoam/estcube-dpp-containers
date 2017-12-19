import { Component, Input } from '@angular/core';

@Component({
  moduleId: module.id,
  selector   : 'spinner-component',
  templateUrl: 'spinner.component.html',
  styleUrls  : ['spinner.component.css']
})

export class SpinnerComponent {

  // input from parent component to make the spinner small (used on buttons)
  @Input() small: boolean;
  constructor() {}

}
