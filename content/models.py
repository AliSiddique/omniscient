from email import message
from unicodedata import name
from django.db import models

from user.models import Profile
from payment.models import Pricing
# Create your models here.
CHOICES =(
    ("Economy", "Economy"),
    ("Finance", "Finance"),
    ("Politics", "Politics"),
    ("Technology", "Technology"),
    ("Sports", "Sports"),
    ("Uni","University"),
    ("Media","Media")
)
class Article(models.Model):
    writer=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=4500)
    slug=models.SlugField(max_length=30, blank=True,  null=True,unique=True)
    favourites = models.ManyToManyField(Profile,related_name='favourites',default=None,blank=True)
    views = models.BigIntegerField()
    pricing_tiers = models.ManyToManyField(Pricing,blank=True)
    image = models.ImageField()
    category = models.CharField(choices=CHOICES,max_length=100,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)



    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=500,null=True)
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)





class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=300)



YearChoices = (
   ( "Year 10","Year 10"),
   ( "Year 11","Year 11"),
   ( "Year 12","Year 12"),
   ( "Year 13","Year 13"),
   ( "First Year","First Year"),
   ( "Second Year","Second Year"),
   ("Third Year","Third Year"),
   ("Masters Year","Masters"),
   ("Phd ","Phd"),

)
uniChocies = (
    ("University of Aberdeen","University of Aberdeen"),
    ("Abertay University","Abertay University"),
    ("Aberystwyth University","Aberystwyth University"),
    ("Anglia Ruskin University","Anglia Ruskin University"),
    ("Arden University","Arden University"),
    ("Aston University","Aston University"),
    ("Bangor University","Bangor University"),
    ("University of Bath","University of Bath"),
    ("Bath Spa University","Bath Spa University"),
    ("University of Bedfordshire","University of Bedfordshire"),
    ("University of Birmingham","University of Birmingham"),
    ("Birmingham City University","Birmingham City University"),
    ("University College Birmingham","University College Birmingham"),
    ("Bishop Grosseteste University, Lincoln","Bishop Grosseteste University, Lincoln"),
    ("University of Bolton","University of Bolton"),
    ("The Arts University Bournemouth","The Arts University Bournemouth"),
    ("Bournemouth University","Bournemouth University"),
    ("BPP University, private","BPP University, private"),
    ("University of Bradford","University of Bradford"),
    ("University of Brighton","University of Brighton"),
    ("University of Bristol","University of Bristol"),
    ("Brunel University","Brunel University"),
    ("University of Buckingham","University of Buckingham"),
    ("Buckinghamshire New University","Buckinghamshire New University"),

    ("University of Cambridge","University of Cambridge"),
    ("Cardiff University","Cardiff University"),
    ("University of Chester","University of Chester"),
    ("University of Chichester","University of Chichester"),
    ("City university of London","City university of London"),
    ("Coventry University","Coventry University"),
    ("Cranfield University","Cranfield University"),
    ("De Montfort University","De Montfort University"),
    ("University of Derby","University of Derby"),
    ("University of Dundee","University of Dundee"),
    ("Durham University, Durham","Durham University, Durham" ),
    ("University of East Anglia","University of East Anglia"),
    ("University of East London","University of East London"),
    ("Edge Hill University","Edge Hill University"),
    ("University of Edinburgh","University of Edinburgh"),
    ("Edinburgh Napier University","Edinburgh Napier University"),
    ("University of Essex","University of Essex"),
    ("University of Exeter","University of Exeter"),
    ("Falmouth University","Falmouth University"),
    ("University of Glasgow","University of Glasgow"),
    ("Glasgow Caledonian University","Glasgow Caledonian University"),
    ("University of Gloucestershire","University of Gloucestershire"),
    ("University of Greenwich","University of Greenwich"),
    ("Harper Adams University","Harper Adams University"),
    ("Hartpury University","Hartpury University"),
    ("Heriot-Watt University","Heriot-Watt University"),
    ("University of Huddersfield","University of Huddersfield"),
    ("University of Hull","University of Hull"),

    ("Imperial College London" ,"Imperial College London"),
    ("Keele University","Keele University"),
    ("University of Kent","University of Kent"),
    ('Kingston University','Kingston University'),
    ("University of Central Lancashire","University of Central Lancashire"),
    ("Lancaster University","Lancaster University"),

    ("University of Leeds","University of Leeds"),
    ("Leeds Arts University","Leeds Arts University"),
    ('Leeds Beckett University','Leeds Beckett University'),
    ("Leeds Trinity University","Leeds Trinity University"),
    ("University of Leicester","University of Leicester"),
    ("University of Lincoln","University of Lincoln"),
    ("University of Liverpool","University of Liverpool"),
    ("Liverpool Hope University","Liverpool Hope University"),
    ("Liverpool John Moores University","Liverpool John Moores University"),
    ("University of London","University of London"),
    ("London Metropolitan University","London Metropolitan University"),
    ("London South Bank University","London South Bank University"),
    ("Loughborough University","Loughborough University"),
    ("University of Manchester","University of Manchester"),
    ("Manchester Metropolitan University","Manchester Metropolitan University"),
    ("Middlesex University","Middlesex University"),
    ("Newcastle University","Newcastle University"),
    ("Newman University","Newman University"),
    ("University of Northampton","University of Northampton"),
    ("Northumbria University","Northumbria University"),
    ("Norwich University of the Arts","Norwich University of the Arts"),
    ("University of Nottingham","University of Nottingham"),
    ("Nottingham Trent University","Nottingham Trent University"),
    ("The Open University","The Open University"),
    ("University of Oxford","University of Oxford"),
    ("Oxford Brookes University","Oxford Brookes University"),
    ("Plymouth Marjon University" ,"Plymouth Marjon University" ),
    ("Arts University Plymouth","Arts University Plymouth"),
    ("University of Plymouth","University of Plymouth"),
    ("University of Portsmouth","University of Portsmouth"),
    ("Queen Margaret University","Queen Margaret University"),
    ("Queen's University Belfast","Queen's University Belfast"),
    ("Ravensbourne University","Ravensbourne University"),
    ("University of Reading","University of Reading"),
    ("Regent's University London","Regent's University London"),
    ("The Robert Gordon University","The Robert Gordon University"),
    ("Roehampton University","Roehampton University"),
    ("Royal Agricultural University, Cirencester","Royal Agricultural University, Cirencester"),
    ("University of Salford","University of Salford"),
    ("University of Sheffield","University of Sheffield"),
    ("Sheffield Hallam University","Sheffield Hallam University"),
    ("University of South Wales","University of South Wales"),
    ("University of Southampton","University of Southampton"),
    ("Solent University","Solent University"),
    ("University of St Andrews","University of St Andrews"),
    ("St Mary's University","St Mary's University"),
    ("Staffordshire University","Staffordshire University"),
    ("University of Stirling, Bridge of Allan","University of Stirling, Bridge of Allan"),
    ("University of Strathclyde","University of Strathclyde"),
    ("University of Strathclyde, Glasgow","University of Strathclyde, Glasgow"),
    ("University of Suffolk, Ipswich, Bury St Edmunds, Great Yarmouth, Lowestoft","University of Suffolk, Ipswich, Bury St Edmunds, Great Yarmouth, Lowestoft"),
    ("University of Sunderland","University of Sunderland"),
    ("University of Surrey, Guildford","University of Surrey, Guildford"),
    ("University of Sussex","University of Sussex"),
    ("Swansea University","Swansea University"),
    ("Teesside University, Middlesbrough and Darlington","Teesside University, Middlesbrough and Darlington"),

    ("University of Ulster, Belfast","University of Ulster, Belfast"),
    ("University of the Arts London","University of the Arts London"),
    ("Ulster University, Coleraine, Jordanstown, Magee and Belfast","Ulster University, Coleraine, Jordanstown, Magee and Belfast"),
    ("University of Law","University of Law"),
    ("University of Wales","University of Wales"),
    ("University of Warwick, Coventry","University of Warwick, Coventry"),
    ("University of the West of England, Bristol","University of the West of England, Bristol"),
    ("University of the West of Scotland, Paisley, Hamilton, Ayr & Dumfries","University of the West of Scotland, Paisley, Hamilton, Ayr & Dumfries"),
    ("University of West London, Ealing and Brentford","University of West London, Ealing and Brentford"),
    ("University of Westminster","University of Westminster"),
    ("University of Winchester","University of Winchester"),
    ("University of Wolverhampton","University of Wolverhampton"),
    ("University of Worcester","University of Worcester"),
    ("Wrexham Glyndŵr University","Wrexham Glyndŵr University"),
    ("University of York","University of York"),
    ("York St John University","York St John University")

)

class BecomeWriter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    year = models.CharField(choices=YearChoices,max_length=50)
    univeristy = models.CharField(choices=uniChocies,max_length=100)
    course= models.CharField(max_length=50,default='')
    file= models.FileField()
    accepted = models.BooleanField(default=False)

