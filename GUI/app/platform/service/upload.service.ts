import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/share';

@Injectable()

export class UploadService {



    makeFileRequest(url: string, params: Array<string>, file: File)
        : Observable<any> 
    {

        return Observable.create(obs => {
            var formData: any = new FormData();
            var xhr = new XMLHttpRequest();
            
            formData.append("file", file, file.name);
            
            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        obs.next(JSON.parse(xhr.response));
                        obs.complete();
                        console.log("Request complete");
                    } else {
                        obs.error(xhr.response);
                    }
                }
            };

            xhr.open('POST', url, true);
            console.log("Request opened");
            xhr.send(formData);
            console.log("Request sent");
        },
        err => { return Observable.throw(err); });





    }

}