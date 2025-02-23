#! /usr/local/bin/perl
if(! -r $ARGV[0])  {print "Please check the $ARGV[0] file!!\n";exit 101;}
my %DieError=();
my %LXXYY=();
my %DXXYY=();
my @SumRLC=();
my @SumFail=();
my @TitRLC=();
my $DieRLC=0;
my $TotalDie=0;
my %TTRRLC=();
my %LstRLC=();
my %T25503XY=();
my %T25383XY=();
my %FileLTX=();
my %FileLTY=();
my %FileLTZ=();
my @FileAPTI=();
my $FillXY="";
#my $Out_File="new_".$ARGV[0];
#open FF,">$Out_File";
#binmode(FF);

SC2K1D_CorrectMap($ARGV[0],8);#Correct Map & extend 8die-group to 1die
#SC2K1D_CorrectMap($ARGV[0],0);#Correct Map

#close(FF);


#-------------------------------------------------------------------------------------------------------------------

sub SC2K1D_CorrectMap
{
  my $filesize = 0;
  my $LineFeed=chr(10);
  my $DOSLineFeed=chr(13).chr(10);
  my $UNIXLineFeed=chr(10);
  my $TABCode=chr(9);

  my $OpenFile=$_[0];
  my $Group2Die=$_[1];
  my $FullFile="";
  my $FullByLine=();
  my %ZCodeSum=();
  my %ZCodefin=();
  my $TotalPass=0;
  my $filesize = (stat("$OpenFile"))[7];
  open GG,"$OpenFile";
  binmode(GG);
  read(GG,$FullFile,$filesize);
  close GG;

  $FullFile=~s/$DOSLineFeed/$LineFeed/g;
  @FullByLine=split($LineFeed,$FullFile);

  for(my $i=0;$i<$#FullByLine+1;$i++)
  {
    my $EachLine="";
    $EachLine=$FullByLine[$i];
    
    if($EachLine =~/X(...),Y(...),A(....),B(.*)/)
    {
      my $XXX=$1;
      my $YYY=$2;
      my $AAA=$3;
      my $BBB=$4;
      if($AAA>16)
      {
        $YYY=$YYY+11;
        $EachLine=sprintf("X%03d,Y%03d,A%04d,B%s",$XXX,$YYY,$AAA,$BBB);
      }
      if($Group2Die>0)
      {
        if($EachLine =~/X(...),Y(...),A(.*)/)
        {
          my $XXX=$1;
          my $YYY=$2;
          my $AAA=$3;
          my $DDX=($XXX-17)*2+5;
          my $DDY=($YYY-16)*4+5;
          my $EachLine1=sprintf("X%03d,Y%03d,A%s\n",$DDX+0,$DDY+0,$AAA);
          my $EachLine2=sprintf("X%03d,Y%03d,A%s\n",$DDX+1,$DDY+0,$AAA);
          my $EachLine3=sprintf("X%03d,Y%03d,A%s\n",$DDX+0,$DDY+1,$AAA);
          my $EachLine4=sprintf("X%03d,Y%03d,A%s\n",$DDX+1,$DDY+1,$AAA);
          my $EachLine5=sprintf("X%03d,Y%03d,A%s\n",$DDX+0,$DDY+2,$AAA);
          my $EachLine6=sprintf("X%03d,Y%03d,A%s\n",$DDX+1,$DDY+2,$AAA);
          my $EachLine7=sprintf("X%03d,Y%03d,A%s\n",$DDX+0,$DDY+3,$AAA);
          my $EachLine8=sprintf("X%03d,Y%03d,A%s",$DDX+1,$DDY+3,$AAA);
          $EachLine=$EachLine1.$EachLine2.$EachLine3.$EachLine4.$EachLine5.$EachLine6.$EachLine7.$EachLine8;
        }
      }
    }
    
    if($Group2Die>0 && $EachLine =~/WAFEREND/)
    {
      SC2K1D_FillB01();
      printf "%s\n",$FillXY;
    }
    printf "%s\n",$EachLine;
  }
  #printf "\n0,%s, , ,%d\n",$OpenFile,$TotalPass;
}
