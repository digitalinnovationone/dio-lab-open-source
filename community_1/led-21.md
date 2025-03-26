# Adriano Godoy

Me chamo Adriano, sou engenheiro, já fiz muitos projetos em diversas áreas, sei programar em várias linguagens, sendo a principal C#. 

## conecta-se comigo:
[![Gmail](https://img.shields.io/badge/Gmail-660066?style=for-the-badge&logo=gmail&logoColor=black)](mailto:adriano.godoy@gmail.com) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-660066?style=for-the-badge&logo=linkedin&logoColor=black)](https://www.linkedin.com/in/adriano-lopes-godoy-84246051/) 
:--------: | :------: 

 ## Tecnologias: 

![.NET](https://img.shields.io/badge/.NET-5C2D91?style=for-the-badge&logo=.net&logoColor=white) | ![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white)| ![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white) | ![Java](https://img.shields.io/badge/Java-660066?style=for-the-badge&logo=java) | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) | ![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white) | ![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white) | ![SQLite](https://img.shields.io/badge/SQLite-000?style=for-the-badge&logo=sqlite&logoColor=07405E) | ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
:--------: | :------: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: | 

## Liguagens mais usadas

![Top Langs](https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=led-21&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF)

No repositorio aparece como C++ por ser a linguagem que uso em tutoriais e para programar microcontroladores.

## Exemplo de Código API Mínima | AspNetCore | Signal R 
```
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.EntityFrameworkCore;
using BlazorServerSignalR;
using BlazorServerSignalR.Data;
using Microsoft.AspNetCore.ResponseCompression;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddSingleton<ArduinoService>();

builder.Services.AddDbContext<DbContext>
  (opt => opt.UseInMemoryDatabase("MessageList"));

builder.Services.AddResponseCompression(opts =>
{
    opts.MimeTypes = ResponseCompressionDefaults.MimeTypes.Concat(
        new[] { "application/octet-stream" });
});

var app = builder.Build();

app.UseResponseCompression();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseRouting();

app.MapBlazorHub();

app.MapHub<ChatHub>("/chathub");
app.MapFallbackToPage("/_Host");

app.Run();
```