import json,urllib2
import time
from collections import OrderedDict

ics_code = {
1000002:'Acton Town Underground Station',
1000003:'Aldgate Underground Station',
1000004:'Aldgate East Underground Station',
1000005:'Alperton Underground Station',
1000006:'Amersham Rail Station',
1000007:'Angel Underground Station',
1000008:'Archway Underground Station',
1000009:'Arnos Grove Underground Station',
1000010:'Arsenal Underground Station',
1000011:'Baker Street Underground Station',
1000012:'Balham',
1000013:'Bank Underground Station',
1000014:'Barbican Underground Station',
1000015:'Barking Underground Station',
1000016:'Barkingside Underground Station',
1000017:'Barons Court Underground Station',
1000018:'Bayswater Underground Station',
1000019:'Becontree Underground Station',
1000020:'Belsize Park Underground Station',
1000021:'Bermondsey Underground Station',
1000022:'Bethnal Green Underground Station',
1000023:'Blackfriars Underground Station',
1000024:'Blackhorse Road Underground Station',
1000025:'Bond Street Underground Station',
1000026:'Borough Underground Station',
1000027:'Boston Manor Underground Station',
1000028:'Bounds Green Underground Station',
1000029:'Bow Road Underground Station',
1000030:'Brent Cross Underground Station',
1000031:'Brixton Underground Station',
1000032:'Bromley-By-Bow Underground Station',
1000033:'Buckhurst Hill Underground Station',
1000034:'Burnt Oak Underground Station',
1000035:'Caledonian Road Underground Station',
1000036:'Camden Town Underground Station',
1000037:'Canada Water Underground Station',
1000038:'Canary Wharf Underground Station',
1000039:'Canning Town Underground Station',
1000040:'Cannon Street Underground Station',
1000041:'Canons Park Underground Station',
1000042:'Chalfont & Latimer Rail Station',
1000043:'Chalk Farm Underground Station',
1000044:'Chancery Lane Underground Station',
1000045:'Charing Cross Underground Station',
1000046:'Chesham',
1000047:'Chigwell Underground Station',
1000048:'Chiswick Park Underground Station',
1000049:'Chorleywood Underground Station',
1000050:'Clapham Common Underground Station',
1000051:'Clapham North Underground Station',
1000052:'Clapham South Underground Station',
1000053:'Cockfosters Underground Station',
1000054:'Colindale Underground Station',
1000055:'Colliers Wood Underground Station',
1000056:'Covent Garden, Covent Garden',
1000057:'Croxley Underground Station',
1000058:'Dagenham East Underground Station',
1000059:'Dagenham Heathway Underground Station',
1000060:'Debden Underground Station',
1000061:'Dollis Hill Underground Station',
1000062:'Ealing Broadway Rail Station',
1000063:'Ealing Common Underground Station',
1000064:'Earl\'s Court Underground Station',
1000065:'East Acton Underground Station',
1000066:'Eastcote Underground Station',
1000067:'East Finchley Underground Station',
1000068:'East Ham Underground Station',
1000069:'East Putney Underground Station',
1000070:'Edgware Underground Station',
1000071:'Edgware Road - Stop EC',
1000072:'Edgware Road (Circle Line) Underground Station',
1000073:'Elephant & Castle Underground Station',
1000074:'Elm Park Underground Station',
1000075:'Embankment Underground Station',
1000076:'Epping Underground Station',
1000077:'Euston Underground Station',
1000078:'Euston Square Underground Station',
1000079:'Fairlop Underground Station',
1000080:'Farringdon Underground Station',
1000081:'Finchley Central Underground Station',
1000082:'Finchley Road Underground Station',
1000083:'Finsbury Park Underground Station',
1000084:'Fulham Broadway Underground Station',
1000085:'Gants Hill Underground Station',
1000086:'Gloucester Road Underground Station',
1000087:'Golders Green Underground Station',
1000088:'Goldhawk Road Underground Station',
1000089:'Goodge Street Underground Station',
1000090:'Grange Hill Underground Station',
1000091:'Great Portland Street Underground Station',
1000092:'Greenford Underground Station',
1000093:'Green Park Underground Station',
1000094:'Gunnersbury Underground Station',
1000095:'Hainault Underground Station',
1000096:'Hammersmith (Dist&Picc Line) Underground Station',
1000097:'Hammersmith (H&C Line) Underground Station',
1000098:'Hampstead Underground Station',
1000099:'Hanger Lane Underground Station',
1000100:'Harlesden Station - Stop HA',
1000101:'Harrow & Wealdstone Station - Stop M',
1000102:'Harrow Bus Station - Stop B',
1000103:'Hatton Cross Station - Stop E',
1000104:'Heathrow Terminal 4 - Stop 6',
1000105:'Heathrow Terminals 1-2-3 Underground Station',
1000106:'Hendon Central Underground Station',
1000107:'High Barnet Underground Station',
1000108:'Highbury & Islington Underground Station',
1000109:'Highgate Underground Station',
1000110:'High Street Kensington Underground Station',
1000111:'Hillingdon Underground Station',
1000112:'Holborn Underground Station',
1000113:'Holland Park Underground Station',
1000114:'Holloway Road Underground Station',
1000115:'Hornchurch Underground Station',
1000116:'Hounslow Central Underground Station',
1000117:'Hounslow East Underground Station',
1000118:'Hounslow West Underground Station',
1000119:'Hyde Park Corner Underground Station',
1000120:'Ickenham Underground Station',
1000121:'Kennington Underground Station',
1000122:'Kensal Green Underground Station',
1000123:'Kentish Town Underground Station',
1000124:'Kenton',
1000125:'Kew Gardens Underground Station',
1000126:'Kilburn Underground Station',
1000127:'Kilburn Park Underground Station',
1000128:'Kingsbury Underground Station',
1000129:'King\'s Cross St.Pancras Underground Station',
1000130:'Knightsbridge Underground Station',
1000131:'Ladbroke Grove Underground Station',
1000132:'Lambeth North Underground Station',
1000133:'Lancaster Gate',
1000134:'Latimer Road Underground Station',
1000135:'Leicester Square Underground Station',
1000136:'Leyton Underground Station',
1000137:'Leytonstone Underground Station',
1000138:'Liverpool Street Underground Station',
1000139:'London Bridge Underground Station',
1000140:'Loughton Underground Station',
1000141:'Maida Vale Underground Station',
1000142:'Manor House Underground Station',
1000143:'Mansion House Underground Station',
1000144:'Marble Arch Underground Station',
1000145:'Marylebone Underground Station',
1000146:'Mile End Underground Station',
1000147:'Mill Hill East Underground Station',
1000148:'Monument Underground Station',
1000149:'Moorgate Underground Station',
1000150:'Moor Park Underground Station',
1000151:'Morden Underground Station',
1000152:'Mornington Crescent Underground Station',
1000153:'Neasden Underground Station',
1000154:'Newbury Park Underground Station',
1000155:'New Cross Station',
1000156:'New Cross Gate',
1000157:'North Acton Underground Station',
1000158:'North Ealing Underground Station',
1000159:'Northfields Underground Station',
1000160:'North Greenwich Underground Station',
1000161:'North Harrow Underground Station',
1000162:'Northolt Station - Stop B',
1000163:'North Wembley',
1000164:'Northwick Park Underground Station',
1000165:'Northwood Underground Station',
1000166:'Northwood Hills Underground Station',
1000167:'Notting Hill Gate Underground Station',
1000168:'Oakwood Underground Station',
1000169:'Old Street Underground Station',
1000170:'Kensington (Olympia) Station',
1000171:'Osterley Underground Station',
1000172:'Oval Underground Station',
1000173:'Oxford Circus Underground Station',
1000174:'Paddington',
1000175:'Paddington (H&C Line)',
1000176:'Park Royal Underground Station',
1000177:'Parsons Green Underground Station',
1000178:'Perivale Underground Station',
1000179:'Piccadilly Circus Underground Station',
1000180:'Pimlico Underground Station',
1000181:'Pinner Station - Stop C',
1000182:'Plaistow Underground Station',
1000183:'Preston Road Underground Station',
1000184:'Putney Bridge Underground Station',
1000185:'Queensbury Underground Station',
1000186:'Queen\'s Park Underground Station',
1000187:'Queensway Underground Station',
1000188:'Ravenscourt Park Underground Station',
1000189:'Rayners Lane Underground Station',
1000190:'Redbridge Underground Station',
1000191:'Regent\'s Park Underground Station',
1000192:'Richmond Rail Station',
1000193:'Rickmansworth Underground Station',
1000194:'Roding Valley Underground Station',
1000195:'Rotherhithe',
1000196:'Royal Oak Underground Station',
1000197:'Ruislip Underground Station',
1000198:'Ruislip Gardens Underground Station',
1000199:'Ruislip Manor Underground Station',
1000200:'Russell Square Underground Station',
1000201:'Seven Sisters Underground Station',
1000202:'Shadwell DLR',
1000203:'Shepherd\'s Bush (Central Line) - Stop F',
1000204:'Shepherd\'s Bush Market Underground Station',
1000205:'Theydon Bois, Theydon Bois Green',
1000206:'Sloane Square Underground Station',
1000207:'Snaresbrook Underground Station',
1000208:'South Ealing Underground Station',
1000209:'Southfields Underground Station',
1000210:'Southgate Underground Station',
1000211:'South Harrow Station - Stop G',
1000212:'South Kensington Underground Station',
1000213:'South Kenton',
1000214:'South Ruislip Underground Station',
1000215:'Southwark Underground Station',
1000216:'South Wimbledon Underground Station',
1000217:'South Woodford Underground Station',
1000218:'Stamford Brook Underground Station',
1000219:'Stanmore Underground Station',
1000220:'Stepney Green Underground Station',
1000221:'St. James\'s Park Underground Station',
1000222:'St John\'s Wood Underground Station',
1000223:'Stockwell Underground Station',
1000224:'Stonebridge Park Underground Station',
1000225:'St. Paul\'s Underground Station',
1000226:'Stratford Underground Station',
1000227:'Sudbury Hill Underground Station',
1000228:'Sudbury Town Underground Station',
1000229:'Surrey Quays',
1000230:'Swiss Cottage Underground Station',
1000231:'Temple Underground Station',
1000232:'Theydon Bois Underground Station',
1000233:'Tooting Bec Underground Station',
1000234:'Tooting Broadway Underground Station',
1000235:'Tottenham Court Road Underground Station',
1000236:'Tottenham Hale Underground Station',
1000237:'Totteridge & Whetstone Underground Station',
1000238:'Tower Hill Underground Station',
1000239:'Tufnell Park Station - Stop TN',
1000240:'Turnham Green Underground Station',
1000241:'Turnpike Lane Underground Station',
1000242:'Upminster Rail Station',
1000243:'Upminster Bridge Underground Station',
1000244:'Upney Underground Station',
1000245:'Upton Park Underground Station',
1000246:'Uxbridge Station - Stop M',
1000247:'Vauxhall Underground Station',
1000248:'Victoria',
1000249:'Walthamstow Central Underground Station',
1000250:'Wanstead Underground Station',
1000251:'Wapping',
1000252:'Warren Street Underground Station',
1000253:'Warwick Avenue Underground Station',
1000254:'Waterloo Underground Station',
1000255:'Watford Underground Station',
1000256:'Wembley Central Station - Stop CT',
1000257:'Wembley Park Underground Station',
1000258:'West Acton Underground Station',
1000259:'Westbourne Park Underground Station',
1000260:'West Brompton Underground Station',
1000261:'West Finchley Underground Station',
1000262:'West Ham Underground Station',
1000263:'West Hampstead Underground Station',
1000264:'West Harrow',
1000265:'West Kensington Underground Station',
1000266:'Westminster Underground Station',
1000267:'West Ruislip Underground Station',
1000268:'Whitechapel Underground Station',
1000269:'White City Underground Station',
1000270:'Willesden Green Underground Station',
1000271:'Willesden Junction',
1000272:'Wimbledon Underground Station',
1000273:'Wimbledon Park Underground Station',
1000274:'Woodford Underground Station',
1000275:'Wood Green Underground Station',
1000276:'Woodside Park Underground Station',
1000277:'Northumberland Gardens - Stop ->S',
1000278:'Wood Lane',
1000279:'Croydon (London), Addiscombe Road - Stop E5',
1000280:'Bushey, Bushey Railway Station West',
1000281:'Dagenham East, Dagenham, Reede Road - Stop ->S',
1000282:'Ringers Road - Stop C',
1000283:'Brabham Court - Stop ->N',
1000284:'Lambrook Terrace - Stop FQ',
1000286:'Nelson\'s Row - Stop B',
1000287:'Sir Ludwig Guttmann Health Centre - Stop R',
1000288:'Clapham Common, Omnibus Clapham',
1000289:'Creekmouth, Rivergate Centre',
1000290:'Brentford, Great West Quarter - Stop BY',
1000291:'Brookmans Park Rail Station',
1000292:'Brentwood Rail Station',
1000293:'Brookmans Park, Brookmans Park Railway Station - Stop A',
1000294:'Brentwood, Brentwood Railway Station',
1000295:'Bushey, Bushey Railway Station East',
1000296:'Chorleywood, Chorleywood Railway Station',
1000297:'White Post Lane - Stop D',
1000298:'Upper Sydenham, High Level Drive',
1000299:'Amersham, Railway Station',
1000300:'Tudway Road - Stop ->N',
1000301:'Kidbrooke Park Road - Stop ->N',
1000302:'Little Chalfont, Station Forecourt',
1000303:'Little Chalfont, Railway Station',
1000304:'Chesham (Bucks), Chesham Underground Station',
1000305:'Chesham (Bucks), Broadway',
1000306:'Rickmansworth, Rickmansworth Railway Station',
1000307:'Croxley Green, Hazelwood Road',
1000308:'Croxley Green, Croxley Metropolitan Station - Stop ->SE',
1000309:'Cassiobury Park, Watford Metropolitan Station',
1000310:'Moor Park (Herts), Moor Park Station',
1000311:'Watford (Herts), Watford Junction Railway Station',
1000312:'Watford (Herts), Watford High Street Railway Station - Stop B',
1000313:'Watford (Herts), Tesco - Stop ->SE',
1000314:'Epping, Epping Station',
1000315:'South Oxhey, Carpenders Park Railway Station',
1000316:'Loughton (Essex), Loughton Station',
1000317:'Buckhurst Hill, Buckhurst Hill Station',
1000319:'Chigwell, Chigwell Station',
1000320:'Grange Hill, Grange Hill Station',
1000321:'West Hampstead, West Hampstead Rail Station',
1000325:'Brixton Rail Station',
1000326:'Elephant & Castle Rail Station',
1000327:'Beckenham Junction Tram Stop',
1000328:'Balham Rail Station',
1000329:'Shadwell Rail Station',
1000330:'Birkbeck Rail Station',
1000331:'Birkbeck Station',
1000332:'Lewisham Rail Station',
1000333:'Highbury (London), Highbury Barn',
1000334:'Finsbury Park Rail Station',
1000335:'Coombe Lane West / New Victoria Hospital - Stop >N',
1000336:'East Croydon Tram Stop',
1000337:'Cannon Street, Cannon Street Rail Station',
1000338:'Beaconsfield Rail Station',
1000339:'Great Missenden, Railway Station',
1000340:'Watford (Herts), Waterfields Way - Stop ->S',
1000341:'Brandville Gardens - Stop Y',
1000342:'Southfield Gardens - Stop SF',
1000343:'Buckingham Road / Harlesden - Stop B',
1000344:'Vauxhall (London), Vauxhall Rail Station',
1000345:'Hallsville Road - Stop ->NE',
1000346:'Carpenters Primary School - Stop >SE',
1000347:'Wingate Square - Stop ->S',
1000348:'Barnehurst Avenue - Stop J',
1000349:'Rush Green Road / Dagenham Road - Stop J',
1000350:'Kingsway / Holborn Station - Stop M',
1000351:'Marylebone Station - Stop P'
}

class HomePlanner:
    def __init__(self, destination_count = 2, start_station = 1000002, end_station = 1000352, result_limit = 10, abs_diff_limit = 23):
        self.start_station = start_station
        self.end_station = end_station
        self.destination_count = destination_count
        self.result_limit = result_limit
        self.abs_diff_limit = abs_diff_limit
        self.postcode = []
        self.final_dic = {}
        self.d_add = {}
        
    def input_dest(self):
        for i in range(self.destination_count):
            raw_p = raw_input("Input postcode {}: ".format(i+1))
            self.postcode.append(raw_p.replace(' ',''))
    
    def add_destination(self, postcode):
        self.postcode.append(postcode.replace(' ',''))


    def populate_res(self):
        st = time.time()
        for p in self.postcode:
          duration_dic = {}
          for i in range(self.start_station, self.end_station):
            if i == 175:
                print "Sleeping for 1 min and wait for api limit"
                time.sleep(62)
            # 
            url = "https://api.tfl.gov.uk/Journey/JourneyResults/{0}/to/{1}?nationalSearch=False&timeIs=Departing&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&app_id=0566e0a5&app_key=77f47ea629c3de976f0a3926c04a03f9".format(i, p)
            l = json.loads(urllib2.urlopen(url).read())
            shortest = 100000
            if 'journeys' in l:
                #print '{0}:\'{1}\','.format(l['journeys'][0]['legs'][0]['departurePoint']['icsCode'], l['journeys'][0]['legs'][0]['departurePoint']['commonName'])
                for item in l['journeys']:
                    if item['duration'] < shortest:
                        shortest = item['duration']
            duration_dic[i] = shortest
            
          self.final_dic[p] = duration_dic
          print "Searching time {0}".format(time.time() - st)
          print self.final_dic

    def res_reduce(self):
        for key, value in self.final_dic.items():
          for i in range(self.start_station,self.end_station):
            if i in self.d_add:
                self.d_add[i] += value[i]
            else:
                self.d_add[i] = value[i]

    def print_journey(self, l):
        print "Route:"
        for index, journey in enumerate(l['journeys']):
            print "----Journey Choice {0}. Duration {1} min----".format(index+1, journey['duration'])
            for leg in journey['legs']:
                print "{0} -----({1})---- > {2}".format(leg['departurePoint']['commonName'], leg['instruction']['summary'], leg['arrivalPoint']['commonName'])

    def abs_diff(self, value_list,diff):
        sorted_list = sorted(value_list)
        for i in range(len(sorted_list)-1):
            if abs(sorted_list[i]-sorted_list[i+1])>diff:
                return 0
        return 1

    def run(self):
        self.populate_res()
        self.res_reduce()
        d_ordered = OrderedDict(sorted(self.d_add.items(), key=lambda t: t[1]))

        #print d_ordered

        postcode = self.final_dic.keys()

        count = 10
        for key, item in d_ordered.items():
            value_list = [final_dic[p][key] for p in postcode]
            if count>0 and self.abs_diff(value_list, self.abs_diff_limit):
                print "\n------- Best Choice No. {0} --------".format(11-count)
            
                for p in self.postcode:
                    print "Distance to {0}: {1} mins".format( p, self.final_dic[p][key])
                    
                    urlm =  "https://api.tfl.gov.uk/Journey/JourneyResults/{0}/to/{1}?nationalSearch=False&timeIs=Departing&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&app_id=0566e0a5&app_key=77f47ea629c3de976f0a3926c04a03f9".format(key,p)
                    lm = json.loads(urllib2.urlopen(urlm).read())
                    self.print_journey(lm)
                    print ""

            print "--------------------------------------"
            count = count - 1









  
if __name__ == "__main__":
    h = HomePlanner()
    h.input_dest()
    h.run()





 










    


