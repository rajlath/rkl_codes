unit main;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,U_hardwareid;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation


{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
   //edit1.Text := intToStr(U_hardwareid.GetHardwareid);
   //edit1.Text := '';
   edit1.Text := intToStr(U_Hardwareid.CrcString(U_HardwareId.GetCPUSerialNumber));
end;

end.
