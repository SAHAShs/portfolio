import { NgClass, NgFor } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-projects',
  imports: [NgFor,NgClass],
  templateUrl: './projects.component.html',
  styleUrl: './projects.component.scss'
})
export class ProjectsComponent {
flippedIndex: number | null = null;

  projects = [
    {
      title: 'Ship Defect Reporting System',
      stack: '.NET Core MVC + SQL Server',
      icon: 'fa-solid fa-ship',
      iconColor: 'text-indigo-600',
      description: 'Repair tracking system for naval ships with dynamic menus and secure login.'
    },
    {
      title: 'PIMS',
      stack: '.NET Web API + SQL Server + Angular',
      icon: 'fa-solid fa-users',
      iconColor: 'text-blue-500',
      description: 'Employee info system with leave, salary, attendance, and secure role access.'
    },
    {
      title: 'Asset Management System',
      stack: 'Blazor Server + SQL Server + EF Core',
      icon: 'fa-solid fa-store',
      iconColor: 'text-blue-500',
      description: 'Designed and implemented a real-time asset tracking system using Blazor Server and SQL Server.'
    },
     {
      title: 'Transaction Tracker',
      stack: 'Angular + .Net Web API + SQL Server + EF Core',
      icon: 'fa-solid fa-inr',
      iconColor: 'text-blue-500',
      description: 'Designed Transaction tracking system.'
    }
  ];

  flipCard(index: number) {
    this.flippedIndex = this.flippedIndex === index ? null : index;
  }
}
