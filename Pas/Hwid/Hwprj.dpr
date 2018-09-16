program Hwprj;

uses
  Forms,
  main in 'main.pas' {Form1},
  U_Hardwareid in 'U_Hardwareid.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
