import { Component } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = environment.backend_url;

  constructor(protected http: HttpClient) {
    this.http.get<string>(environment.backend_url + '/data').subscribe((title: string) => {
      this.title = title;
     });
  }
}
