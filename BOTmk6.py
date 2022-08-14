import ch
import random
import time
import os
import Tools
from os import path
import sys



class bot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("FFFF00")
    self.setFontColor("000000")
    self.setFontFace("Ariel")
    self.setFontSize(11)

  def onMessage(self, room, user, message):
    print("[{0}] {1}: {2}".format(room.name, user.name.title(), message.body))
      
    try:
      cmd, args = message.body.split(" ", 1)
      
    except:
      cmd, args = message.body, ""
        
    if cmd[0] == "!":
      prfx = True
      cmd = cmd[1:]
      


    ##ROULETTE##
    validBets =["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17",
                "18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33",
                "34","35","36","00","black","red","even","odd"]
    validBets = set(validBets)
    
    validOthers = {"black","red","even","odd"}
    
    validSpin = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17",
                "18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33",
                "34","35","36","00")

    redSpin = ("1","3","5","7","9","12","14","16","18",
                "19","21","23","25","27","30","32","34","36")
    
    blackSpin = ("2","4","6","8","10","11","13","15","17",
                 "20","22","24","26","28","29","31","33","35")
                
    primeSpin = ("2","3","5","7","11","13","17","19","23",
                 "29", "31")

    spinSingles = {}
    spinOthers = {}
    spinColor = ""
    spinParity = ""
    singlesWinnings = 0
    othersWinnings = 0
    
    buxFile=""
    ############
    
    commands = ["!420","!kurt","!kys","!beer","!chief","!weedmo","!ted","!sherk","!mane",
                "!bong","!shotgun","!rape","!dd","!pour","!thisnigga","!what",
                "!jew","!cocaine","!weed","!dafuq","!seph","!knifehit","!monica","!joey",
                "!whatatime","!slowride","!deadniggas","!pstriple","!yablewit","!tanks",
                "!s7", "!cripf","!heem","!sharks","!shot","!pitbull","!whogay","!roll",
                "!random","!shot2","!mid","!loud","!will","!mcs","!pepe","!slots","!2010","!jackoff"
                ,"!prrt", "!tc","!autoloud","!snek","!nigger","!gerbil","!ron","!cig","!mom","!poggers"
                ,"!puggy","!ankh","!poison","!lol","!heroin","!n","!assrape","!ihateniggers","!crippledog",
                "!fuckher","!dmx","!how2roulette","!cocaina","!yajewedit","!milkies","!lopez","!letsgo","!vamos",
                "!cotton","!fwm","!sam","!koth","!eatdick","!spooky","!overdose","!nbomb","!dab","!modelo","!twu","!flamez",
                "!votar", "!fag", "!friday","!trap", "!pahmp", "!dumpit", "!tits", "!ass" , "!puke" , "!hentai",
                "!anime", "!nigstomp", "!tweaker", "!bongo", "!kneel", "!bongstream", "!labonga", "!eagles", "!mc", "!oldmc"]
    
    cheaterdubs = ["11","22","33","44","55","66","77","88","99"]

    slot=["Weed", "Mane", "Nigger", "Jackpot", "Ramen"]

    n= ["https://bongstream.live/wp-content/uploads/2020/04/nigger.jpg","https://bongstream.live/wp-content/uploads/2020/08/N.jpg"] 

    tcposting= ['WAIT WHAT IS GOING ON HERE', 'https://bongstream.live/wp-content/uploads/2022/06/tc-deserve.jpg', 
                'HOLD ON TELL ME FROM THE START PLZ','VROOM VROOM','STOP YOU MUST TELL ME FROM THE BEGINNING WHAT HAPPENED',
                'austrian autist','rain man lol','Im gonna slaughter Ankh'
                ,'Kurt, ive had a long day of being a big shot pilot please inform me of your suffering','!ankh'
                ,'https://bongstream.live/wp-content/uploads/2020/03/tc-koth.png', 'https://bongstream.live/wp-content/uploads/2022/05/will-tc.jpg']

    
    gerb= ['ball rubbin','[gerbilling]',
           'https://bongstream.live/wp-content/uploads/2020/01/gerb-ball-rubbin.jpg',
           'https://bongstream.live/wp-content/uploads/2020/01/take-it.jpg']

    nigs =["https://bongstream.live/wp-content/uploads/2019/11/black5.jpg",
            "https://bongstream.live/wp-content/uploads/2019/11/black1.jpg",
            "https://bongstream.live/wp-content/uploads/2019/11/black4.jpg",
            "https://bongstream.live/wp-content/uploads/2019/11/black2.jpg",
            "https://bongstream.live/wp-content/uploads/2019/11/black3.jpg",]

    mcs= ['Maybe someday.',
        'what?',
        'I dont think so.',
        'No.',
        'Yes.',
        'It is certain.',
        'Nigga why you askin me?',
        'You buggin',
        'Hell yeah.',
        'Idk you do you nigga',
        'Yeah just do it stop askin'
        ]

    pepe= ['https://i.imgur.com/ryDNVDg.jpg','https://i.imgur.com/Hu6PpGQ.png','https://i.imgur.com/StVlN2S.jpg','https://i.imgur.com/4tEdI63.jpg',
        'https://i.imgur.com/bMNLWiX.png','https://i.imgur.com/xxGQnhk.png','https://i.imgur.com/B3OITYc.png','https://i.imgur.com/cMM3sOe.jpg',
        'https://i.imgur.com/voBF7NI.jpg','https://i.imgur.com/ABN17VE.jpg','https://i.imgur.com/jhFVX1m.jpg','https://i.imgur.com/LHfIs2M.png',
        'https://i.imgur.com/iDVX8yN.png','https://i.imgur.com/RAZSCEe.jpg','https://i.imgur.com/mPGZqQK.png',
        'https://i.imgur.com/OOCCeNC.jpg','https://i.imgur.com/ZvepLni.jpg','https://i.imgur.com/nIrtUAz.jpg',
        'https://i.imgur.com/im23gsp.png','https://i.imgur.com/uo764h6.png','https://i.imgur.com/Vli0IYd.jpg',
        'https://i.imgur.com/9dvZZ9z.jpg','https://i.imgur.com/xdA4715.png','https://i.imgur.com/fh696yB.jpg',
        'https://i.imgur.com/hBPitbP.jpg','https://i.imgur.com/IzsgFsn.jpg','https://i.imgur.com/rvF2RHD.png',
        'https://i.imgur.com/tVe4yqp.png','https://i.imgur.com/N1G78e6.jpg','https://i.imgur.com/wNCIdvn.jpg',
        'https://i.imgur.com/7dUjgCv.jpg','https://i.imgur.com/6W3CY9v.jpg','https://i.imgur.com/7Pkiyvq.jpg',
        'https://i.imgur.com/qnDO0cO.jpg','https://i.imgur.com/hzVHpV0.png','https://i.imgur.com/IfcJwqg.jpg',
        'https://i.imgur.com/7Shwa6Y.jpg','https://i.imgur.com/wzPReEa.jpg','https://i.imgur.com/SgVzFtN.png',
        'https://i.imgur.com/CdcZVv0.jpg','https://i.imgur.com/gRwY7ui.jpg','https://i.imgur.com/wzzXD79.png',
        'https://i.imgur.com/FK6AqzF.jpg','https://i.imgur.com/cVoJWwy.jpg','https://i.imgur.com/SSnChGP.png',
        'https://i.imgur.com/PWTW94w.png','https://i.imgur.com/ke0R47g.png','https://i.imgur.com/LKe2jQ3.png',
        'https://i.imgur.com/pi1g5oz.png','https://i.imgur.com/eHhXCiN.png','https://i.imgur.com/ECnkayA.png',
        'https://i.imgur.com/qd1qFdK.png','https://i.imgur.com/krXtmxm.jpg','https://i.imgur.com/BrJkfkq.jpg',
        'https://i.imgur.com/6ZGdbnh.png','https://i.imgur.com/gtriHdl.png','https://i.imgur.com/SX7stsy.png',
        'https://i.imgur.com/Ax86R4D.png','https://i.imgur.com/QsLPMSt.jpg','https://i.imgur.com/0k3AFrd.jpg',
        'https://i.imgur.com/1QHU915.png','https://i.imgur.com/e2e7rH3.png','https://i.imgur.com/dBfemMV.jpg',
        'https://i.imgur.com/YvAtxVo.jpg','https://i.imgur.com/797UOJA.png','https://i.imgur.com/8Wwck9q.jpg',
        'https://i.imgur.com/i8nQkcg.png','https://i.imgur.com/zT1NyeL.jpg','https://i.imgur.com/PfmwiJH.png',
        'https://i.imgur.com/OcfFceE.jpg','https://i.imgur.com/ItxwWj5.jpg','https://i.imgur.com/jse1EXQ.png',
        'https://i.imgur.com/CCw9HcF.jpg','https://i.imgur.com/6z9VJFA.png','https://i.imgur.com/FK6AqzF.jpg',
        ]
    
    titties = ['https://i.ibb.co/cgbB6cZ/Uniform-Glaring-Dromaeosaur-size-restricted.gif', 'https://i.ibb.co/Q9zdBxZ/371846.gif', 'https://i.ibb.co/0FyvVPd/Shimmering-Needy-Emu-size-restricted.gif',
            'https://i.ibb.co/YQNV8WR/beautiful-cocksucker-gets-every-last-drop.gif', 'https://i.ibb.co/CWwCdB9/3777.gif', 'https://i.ibb.co/W6yTYtw/034-1000.gif',
            'https://i.ibb.co/vzYVKpx/036-1000.gif', 'https://i.ibb.co/6RKhJ6V/023-1000.gif', 'https://i.ibb.co/s2YTyfW/020-1000.gif', 'https://i.ibb.co/tc4RtjT/005-1000.gif',
            'https://i.ibb.co/kGFWKP4/994-1000.gif', 'https://i.ibb.co/Rc9YYz4/julebrus-ik4ks-c60803.gif', 'https://i.ibb.co/PQZYbh7/rFlGZ3c.gif', 'https://i.ibb.co/S0HThfK/titty-drop-reveal.gif',
            'https://i.ibb.co/ZWZ591P/hotboobsdropreveal-15823135158c4pl.gif', 'https://i.ibb.co/QQWJtSt/733-1000.gif', 'https://i.ibb.co/0DMKLxR/realnakedgirls-0025.gif',
            'https://i.ibb.co/ZH2vcX7/035-1000.gif', 'https://i.ibb.co/ZG1cvwc/536-1000.gif', 'https://i.ibb.co/MPFVGGk/exploited66-ksi8x-7cd93c.gif', 'https://i.ibb.co/0jGWQY6/333.gif',
            'https://i.ibb.co/hddkMpz/EmaYmZQ.gif', 'https://i.ibb.co/qNYw9s4/respectable-boob-drop.gif', 'https://i.ibb.co/s2YTyfW/020-1000.gif', 'https://i.ibb.co/C6CfmW2/Damp-Red-Iberianmidwifetoad-size-restricted.gif',
            'https://i.ibb.co/sCX82Bz/556-450.gif', 'https://i.ibb.co/PYph5DD/anylovefortanlines-1578155852c48pl.gif', 'https://i.ibb.co/WGHCXTf/Flamboyant-Euphoric-Galapagosdove-size-restricted.gif',
            'https://i.ibb.co/MC76vDN/tumblr-p9h21h-MJGX1xv0plqo1-400.gif', 'https://i.ibb.co/kDLqPND/4DBD106.gif', 'https://i.ibb.co/fqP7btB/727-1000.gif', 'https://i.ibb.co/4Rzz8pM/unnamed.gif',
            'https://i.ibb.co/NCZ6yrK/kwje3jI.gif', 'https://i.ibb.co/5LDp3vT/vhujrn19zva21.gif', 'https://i.ibb.co/VHzMqxS/uioum6oh33uz.gif', 'https://i.ibb.co/NtWDDj2/tumblr-pdlyf8063b1xc5zrlo1-400.gif',
            'https://i.ibb.co/kmW934s/tits33.gif', 'https://i.ibb.co/mcpYrLj/tits32.gif', 'https://i.ibb.co/7bV3b3s/tits31.gif', 'https://i.ibb.co/Khbxv9q/tits30.gif', 'https://i.ibb.co/V9XrP6c/tits29.gif',
            'https://i.ibb.co/bJkT8JG/tits28.gif', 'https://i.ibb.co/VVzZgBZ/tits27.gif', 'https://i.ibb.co/qxpBY9n/tits26.gif', 'https://i.ibb.co/JrG999P/tits25.gif', 'https://i.ibb.co/MC8wJSZ/tits24.gif',
            'https://i.ibb.co/Yb7rKf3/tits23.gif', 'https://i.ibb.co/zN20PXk/tits22.gif', 'https://i.ibb.co/b1gfh9S/tits21.gif', 'https://i.ibb.co/LQrJ5vQ/tits20.gif', 'https://i.ibb.co/q09J78d/tits19.gif',
            'https://i.ibb.co/C0bZXkS/tits18.gif', 'https://i.ibb.co/T13frKW/tits17.gif', 'https://i.ibb.co/ZV39Ms6/tits16.gif', 'https://i.ibb.co/QDXcgnN/tits15.gif', 'https://i.ibb.co/R6YNXVh/tits14.gif',
            'https://i.ibb.co/w6DN7L6/tits13.gif', 'https://i.ibb.co/rHk40Nj/tits12.gif', 'https://i.ibb.co/9sSQCy1/tits11.gif', 'https://i.ibb.co/4fjGc2G/tits10.gif', 'https://i.ibb.co/kXQrTJD/tits09.gif',
            'https://i.ibb.co/Kh9zMnT/tits08.gif', 'https://i.ibb.co/vw0BQf4/tits07.gif', 'https://i.ibb.co/6ZXLyvh/tits06.gif', 'https://i.ibb.co/8XPT25B/tits05.gif', 'https://i.ibb.co/gDm1q7n/tits04.gif',
            'https://i.ibb.co/Yc9QRBw/tits02.gif', 'https://i.ibb.co/J7ZfDdc/tits01.gif']


    ass = ['https://i.ibb.co/Z8R7vjs/ass-22.gif', 'https://i.ibb.co/gZY0MpQ/ass-21.gif', 'https://i.ibb.co/JpM87xy/ass-20.gif', 'https://i.ibb.co/899kbvL/ass-19.gif', 'https://i.ibb.co/Y27g07c/ass-18.gif',
           'https://i.ibb.co/KN18nFk/ass-17.gif', 'https://i.ibb.co/kHKCNMy/ass-16.gif', 'https://i.ibb.co/XkBJfrQ/ass-15.gif', 'https://i.ibb.co/jGsQGCt/ass-14.gif', 'https://i.ibb.co/sPzh7cm/ass-13.gif',
           'https://i.ibb.co/3FMGhGX/ass-12.gif', 'https://i.ibb.co/swFj3f5/ass-11.gif', 'https://i.ibb.co/CHj6Zbd/ass-10.gif', 'https://i.ibb.co/KFncDtD/ass-9.gif', 'https://i.ibb.co/SXg7cd8/ass-8.gif',
           'https://i.ibb.co/10zj1DJ/ass-7.gif', 'https://i.ibb.co/hsBdsfM/ass-6.gif', 'https://i.ibb.co/8XsMSJj/ass-5.gif', 'https://i.ibb.co/cFqG1cW/ass-4.gif', 'https://i.ibb.co/Zc8NFny/ass-3.gif',
           'https://i.ibb.co/JdQ7Wcj/ass-2.gif', 'https://i.ibb.co/6mwdRRG/ass-1.gif', 'https://i.ibb.co/mtLddrj/butt29.gif', 'https://i.ibb.co/VxNxwjL/butt28.gif', 'https://i.ibb.co/k5YPfzG/butt27.gif',
           'https://i.ibb.co/qDkWtW4/butt26.gif', 'https://i.ibb.co/Bs757XK/butt25.gif', 'https://i.ibb.co/374wH2L/butt24.gif', 'https://i.ibb.co/grDQYsW/butt23.gif', 'https://i.ibb.co/khfXYPh/butt22.gif',
           'https://i.ibb.co/wc0b6zV/butt21.gif', 'https://i.ibb.co/FD1jXjr/butt20.gif', 'https://i.ibb.co/MPb9XpF/butt18.gif', 'https://i.ibb.co/6mMynL0/butt17.gif', 'https://i.ibb.co/6wsFF5g/butt15.gif',
           'https://i.ibb.co/C9B4nLp/butt14.gif', 'https://i.ibb.co/514JVKr/butt13.gif', 'https://i.ibb.co/yRZcm4T/butt12.gif', 'https://i.ibb.co/hDQ8wNv/butt11.gif', 'https://i.ibb.co/19YcYDn/butt10.gif',
           'https://i.ibb.co/pvNvqvS/butt09.gif', 'https://i.ibb.co/6Xc8jf9/butt08.gif', 'https://i.ibb.co/vXr0mvj/butt07.gif', 'https://i.ibb.co/dmDsCpV/butt06.gif', 'https://i.ibb.co/m9Nq0Mn/butt05.gif',
           'https://i.ibb.co/WHM4TNc/butt04.gif', 'https://i.ibb.co/sjYyZNc/butt03.gif', 'https://i.ibb.co/YtTSHBR/butt02.gif', 'https://i.ibb.co/7tZ96bh/butt01.gif']

    hentai = ['https://i.ibb.co/7N1PfZV/tent01.gif', 'https://i.ibb.co/nzsnsmC/tent02.gif', 'https://i.ibb.co/cNVWqQr/tent03.gif',
              'https://i.ibb.co/rwrmntq/tent04.gif', 'https://i.ibb.co/rfzZqNW/tent05.gif', 'https://i.ibb.co/YBp2TLM/tent06.gif',
              'https://i.ibb.co/RCLNyBj/tent07.gif', 'https://i.ibb.co/rmM5d7T/tent08.gif', 'https://i.ibb.co/kcGMXFc/tent09.gif',
              'https://i.ibb.co/yk1cFNZ/tent10.gif', 'https://i.ibb.co/ZHkFbL9/tent11.gif', 'https://i.ibb.co/YRt0PKH/tenor12.gif',
              'https://i.ibb.co/NKNJW58/tent13.gif', 'https://i.ibb.co/kBXH2wh/tent14.gif', 'https://i.ibb.co/wC4SGxS/tent15.gif',
              'https://i.ibb.co/B64xvfz/tent16.gif', 'https://i.ibb.co/ySDYM2y/tent17.gif', 'https://i.ibb.co/VBV2tjp/tent18.gif',
              'https://i.ibb.co/wB2NS7J/tent19.gif', 'https://i.ibb.co/N2Xsg5C/tent20.gif']
    
    anime = ['https://i.ibb.co/7N1PfZV/tent01.gif','https://i.ibb.co/nzsnsmC/tent02.gif','https://i.ibb.co/cNVWqQr/tent03.gif',
              'https://i.ibb.co/rwrmntq/tent04.gif','https://i.ibb.co/rfzZqNW/tent05.gif','https://i.ibb.co/YBp2TLM/tent06.gif',
              'https://i.ibb.co/RCLNyBj/tent07.gif','https://i.ibb.co/rmM5d7T/tent08.gif','https://i.ibb.co/kcGMXFc/tent09.gif',
              'https://i.ibb.co/yk1cFNZ/tent10.gif','https://i.ibb.co/ZHkFbL9/tent11.gif','https://i.ibb.co/YRt0PKH/tenor12.gif',
              'https://i.ibb.co/NKNJW58/tent13.gif','https://i.ibb.co/kBXH2wh/tent14.gif','https://i.ibb.co/wC4SGxS/tent15.gif',
              'https://i.ibb.co/B64xvfz/tent16.gif','https://i.ibb.co/ySDYM2y/tent17.gif','https://i.ibb.co/VBV2tjp/tent18.gif',
              'https://i.ibb.co/wB2NS7J/tent19.gif','https://i.ibb.co/N2Xsg5C/tent20.gif']
    
    koth = ['https://i.ibb.co/894QtQ9/koth30.gif', 'https://i.ibb.co/Jd6WdBJ/koth29.gif', 'https://i.ibb.co/7zRm407/koth28.gif',
            'https://i.ibb.co/LvLCdRB/koth27.gif', 'https://i.ibb.co/1Yc0mbF/koth26.gif', 'https://i.ibb.co/bNYJFc0/koth25.gif',
            'https://i.ibb.co/Vvf5YxQ/koth24.gif', 'https://i.ibb.co/jhcLLNY/koth23.gif', 'https://i.ibb.co/GCt7qXf/koth22.gif',
            'https://i.ibb.co/0tX8xcP/koth21.gif', 'https://i.ibb.co/R6KY99T/koth20.gif', 'https://i.ibb.co/sK95qWD/koth19.gif',
            'https://i.ibb.co/9cCm15M/koth18.gif', 'https://i.ibb.co/gFhJL2H/koth17.gif', 'https://i.ibb.co/gyv7zFN/koth16.gif',
            'https://i.ibb.co/5kBTNBM/koth15.gif', 'https://i.ibb.co/ZHQTGP0/koth14.gif', 'https://i.ibb.co/VmVCqQ6/koth13.gif',
            'https://i.ibb.co/Q8jhjJp/koth12.gif', 'https://i.ibb.co/p2xkPX3/koth11.gif', 'https://i.ibb.co/RThSbbX/koth10.gif',
            'https://i.ibb.co/ZTt4FJg/koth09.gif', 'https://i.ibb.co/W6NqGdK/koth08.gif', 'https://i.ibb.co/qd2NcBx/koth07.gif',
            'https://i.ibb.co/6sPZsyD/koth06.gif', 'https://i.ibb.co/hmFNF47/koth05.gif', 'https://i.ibb.co/QjHBMDx/koth04.gif',
            'https://i.ibb.co/ZVgrTRG/koth03.gif', 'https://i.ibb.co/8jxwwjs/koth02.gif', 'https://i.ibb.co/qyM5Rx7/koth01.gif'
            ,'https://bongstream.live/wp-content/uploads/2022/06/tc-deserve.jpg'] 

    tedSignal = ["https://bongstream.live/wp-content/uploads/2022/05/1-batsignal.jpg"]

    based = ['https://i.ibb.co/kM4WZFT/based.gif']

    levee = ["When the levee breaks ill have no place to stay"]

    woo = ["https://bongstream.live/wp-content/uploads/2020/11/woo.gif"]

    ump = ["https://bongstream.live/wp-content/uploads/2020/11/ump.gif"]

    puke = ['https://i.ibb.co/TkhBLqX/vomit01.gif', 'https://i.ibb.co/LJQ164Y/vomit02.gif',
            'https://i.ibb.co/zbGHGYk/vomit03.gif', 'https://i.ibb.co/7C3Kqwj/vomit04.gif',
            'https://i.ibb.co/GFMg0mX/vomit05.gif', 'https://i.ibb.co/pf8cWGq/vomit06.gif']
    
    ted = ['https://i.ibb.co/92Q5qXL/ted07.jpg', 'https://i.ibb.co/cLd2N6k/ted06.jpg', 'https://i.ibb.co/jbqvp7N/ted05.jpg',
           'https://i.ibb.co/2WzXRLn/ted04.jpg', 'https://i.ibb.co/jhGVSng/ted03.jpg', 'https://i.ibb.co/bg475gK/ted02.jpg',
           'https://i.ibb.co/VYg11Kk/ted01.jpg' ,
           'While I nodded, nearly napping, suddenly there came a clapping. As of ass cheeks gently clapping, clapping at my chamber door. ""Tis a visitor, I muttered, dummy thicc and nothing more.""']

#    whores = ['https://i.ibb.co/1qZPPXx/whore01.gif', 'https://i.ibb.co/fS1BvGc/whore02.gif', 'https://i.ibb.co/yYLvW1x/whore03.gif',
#             'https://i.ibb.co/DwLBv25/whore04.gif', 'https://i.ibb.co/z4LG4Cb/whore05.gif', 'https://i.ibb.co/qJjtDQ6/whore06.gif',
#             'https://i.ibb.co/bbs4rzq/whore07.gif', 'https://i.ibb.co/qDtvwW4/whore08.gif', 'https://i.ibb.co/dQ6YvF4/whore09.gif',
#             'https://i.ibb.co/55GTXQd/whore10.gif', 'https://i.ibb.co/S0JjcDH/whore11.gif', 'https://i.ibb.co/xGMW8Nv/whore12.gif',
#             'https://i.ibb.co/HgK3RjW/whore13.gif', 'https://i.ibb.co/MPwNdxH/whore14.gif', 'https://i.ibb.co/ZmxZ5x9/whore15.gif',
#             'https://i.ibb.co/DQ4nY0R/whore16.gif', 'https://i.ibb.co/K7HQZXK/whore28.gif', 'https://i.ibb.co/S38GLYB/whore27.gif',
#             'https://i.ibb.co/6JSjhmr/whore26.gif', 'https://i.ibb.co/K7HQZXK/whore28.gif', 'https://i.ibb.co/ydCn7rZ/whore24.gif',
#             'https://i.ibb.co/g4syhdX/whore23.gif', 'https://i.ibb.co/X567hpx/whore22.gif', 'https://i.ibb.co/7bYt7Xq/whore21.gif',
#             'https://i.ibb.co/92MSjR9/whore20.gif', 'https://i.ibb.co/XztYm2J/whore19.gif', 'https://i.ibb.co/XjQJHz8/whore18.gif',
#             'https://i.ibb.co/L9N6J89/whore17.gif']

    sluts = ["https://media.oboobs.ru/boobs/17378.jpg", "https://media.oboobs.ru/boobs/17377.jpg", "https://media.oboobs.ru/boobs/17376.jpg", 
             "https://media.oboobs.ru/boobs/17375.jpg", "https://media.oboobs.ru/boobs/17374.jpg", "https://media.oboobs.ru/boobs/17373.jpg",
             "https://media.oboobs.ru/boobs/17372.jpg", "https://media.oboobs.ru/boobs/17371.jpg", "https://media.oboobs.ru/boobs/17370.jpg",
             "https://media.oboobs.ru/boobs/17369.jpg", "https://media.oboobs.ru/boobs/17368.jpg", "https://media.oboobs.ru/boobs/17367.jpg", 
             "https://media.oboobs.ru/boobs/17366.jpg", "https://media.oboobs.ru/boobs/17365.jpg", "https://media.oboobs.ru/boobs/17364.jpg", 
             "https://media.oboobs.ru/boobs/17363.jpg", "https://media.oboobs.ru/boobs/17362.jpg", "https://media.oboobs.ru/boobs/17361.jpg",
             "https://media.oboobs.ru/boobs/17360.jpg", "https://media.oboobs.ru/boobs/17359.jpg", "https://media.oboobs.ru/boobs/17358.jpg", 
             "https://media.oboobs.ru/boobs/17357.jpg", "https://media.oboobs.ru/boobs/17356.jpg", "https://media.oboobs.ru/boobs/17355.jpg",
             "https://media.oboobs.ru/boobs/17354.jpg", "https://media.oboobs.ru/boobs/17353.jpg", "https://media.oboobs.ru/boobs/17352.jpg",
             "https://media.oboobs.ru/boobs/17351.jpg", "https://media.oboobs.ru/boobs/17350.jpg", "https://media.oboobs.ru/boobs/17349.jpg",
             "https://media.oboobs.ru/boobs/17348.jpg", "https://media.oboobs.ru/boobs/17347.jpg", "https://media.oboobs.ru/boobs/17346.jpg",
             "https://media.oboobs.ru/boobs/17345.jpg", "https://media.oboobs.ru/boobs/17344.jpg", "https://media.oboobs.ru/boobs/17343.jpg"]

    mane = ['Das it', 'https://bongstream.live/wp-content/uploads/2020/06/sosa.gif', '!fwm', '!deadniggas',
            '!spooky', '!beer', '!pour', '!thisnigga', '!pstriple', '!dd', '!dmx', "!kneel", "!manekwon",
            'https://bongstream.live/mane']

    north = ["https://bongstream.live/wp-content/uploads/2022/02/18.gif", "https://bongstream.live/wp-content/uploads/2022/02/17.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/16.gif", "https://bongstream.live/wp-content/uploads/2022/02/15.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/14.gif", "https://bongstream.live/wp-content/uploads/2022/02/13.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/12.gif", "https://bongstream.live/wp-content/uploads/2022/02/11.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/10.gif", "https://bongstream.live/wp-content/uploads/2022/02/9.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/8.gif", "https://bongstream.live/wp-content/uploads/2022/02/7.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/6.gif", "https://bongstream.live/wp-content/uploads/2022/02/5.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/4.gif", "https://bongstream.live/wp-content/uploads/2022/02/3.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/2.gif", "https://bongstream.live/wp-content/uploads/2022/02/1.gif",
             "https://bongstream.live/wp-content/uploads/2022/02/20.gif"]

    lmao = ["lmaoo"]

    checkEm = ["https://i.imgur.com/am6jmOG.gif", "https://i.imgur.com/AFBHn16.jpg", "https://i.imgur.com/288LhLk.jpg", "https://i.imgur.com/Iiz4zJz.jpg",
               "https://i.imgur.com/yQTgNuI.jpg", "https://i.imgur.com/47a9x36.jpg", "https://i.imgur.com/bP1WUal.jpg", "https://i.imgur.com/FPuoPE1.jpg",
               "https://i.imgur.com/cyvN4UR.jpg", "https://i.imgur.com/amVJX94.jpg", "https://i.imgur.com/RL4hhza.png", "https://i.imgur.com/MHXU4P8.gif",
               "https://i.imgur.com/fOd8n8E.png", "https://i.imgur.com/NBGlrua.jpg"]


    if message.body.lower().startswith("!tits"):
        room.message(random.choice(titties))

    if message.body.lower().startswith("!sluts"):
        room.message(random.choice(sluts))


    if message.body.lower().startswith("!ass"):
        room.message(random.choice(ass))

    if message.body.lower().startswith("!tna"):
        room.message(random.choice(titties))
        room.message(random.choice(ass))
    
    if message.body.lower().startswith("!tc"):
        room.message(random.choice(tcposting))

    if message.body.lower().startswith("!gerbil"):
        room.message(random.choice(gerb))
  
    if message.body.lower().startswith("!mcs"):
        room.message(random.choice(mcs))

    if message.body.lower().startswith("!pepe"):
        room.message(random.choice(pepe))

    if message.body.lower().startswith("!north"):
        room.message(random.choice(north))

    if message.body.lower().startswith("!mane"):
        room.message(random.choice(mane))

    if message.body.lower().startswith("ayy"):
        room.message(random.choice(lmao))

    if message.body.lower().startswith("wooo"):
        room.message(random.choice(woo))

    if message.body.lower().startswith("banned"):
        room.message(random.choice(ump))

    if message.body.lower().startswith("based"):
        room.message(random.choice(based))

    if message.body.lower().startswith("i miss ted"):
        room.message("THE")
        room.message("BONGO")
        room.message("KING")
        
##    if message.body.lower().find("ted") > -1:
##       room.message(random.choice(tedSignal))

    if message.body.lower().startswith("!hentai"):
        room.message(random.choice(hentai))

    if message.body.lower().startswith("anime"):
        room.message(random.choice(anime))

    if message.body.lower().startswith("!koth"):
        room.message(random.choice(koth))

    if message.body.lower().startswith("!ted"):
        room.message(random.choice(ted))

    if message.body.lower().startswith("anons"):
        if message.body.lower().find("hang") > -1:
            room.message("https://bongstream.live/wp-content/uploads/2022/05/noose-png-35248.png")

    if cmd.lower() == "420" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2022/05/weed-time-weed.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "2010" and prfx:
      room.message("https://i.redd.it/c60z7efh71a21.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "kurt" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/02/l_153.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "kys":
      room.message("https://bongstream.live/wp-content/uploads/2019/08/kys.jpg".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "beer" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/stonecold.gif".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "chief" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/IMG_0203.jpg".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "weedmo" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/free-kurt.mp3".format(room.name, user.name.title(), message.body))
     
    if cmd.lower() == "sherk" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/chip.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "bong" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/bonghouse.png" + " " + "This stream is a GOD DAMN DICTATORSHIP".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "shotgun" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/shotgun.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "rape" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/rape-stop-posting.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "dd" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/dd.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "pour" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/pour.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "thisnigga" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/thisnigga.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "what?":
      room.message("https://bongstream.live/wp-content/uploads/2019/08/what.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "jew" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/1111111111.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "nigger" and prfx:
      room.message("https://i.imgur.com/IdD3W8G.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "n":
        room.message("https://bongstream.live/wp-content/uploads/2020/08/N.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "cocaine" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/cocaine.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "weed" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/weed.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "dafuq" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/08/dsfuw.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "seph" and prfx:
      room.message("https://youtu.be/h-ckmPDryus".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "knifehit" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/4_KNIFE_HITS_3_pass_out_stories.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "monica" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/monica.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "whatatime" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/whatatime.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "joey" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/joey.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "slowride" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/slowride.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "nerd" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/nerd.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "deadniggas" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/deadnigga.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "pstriple" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/pstriple.gif".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "yablewit" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/09/yablewit.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "tanks" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/10/tanks-kino.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "cripf" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/10/crip-goodbye.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "heem" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/10/heem.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "sharks" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/10/sharks.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "shot" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/10/Silicon_Valley_Season_6_Bloopers_Reel_-_Behind_the_Scenes_-_HBO.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "pitbull" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/10/pitbull.png".format(room.name, user.name.title(), message.body))    

    if cmd.lower() == "shot2" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/11/shot2.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "will" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/03/sam-keyboard.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "loud" and prfx:
      room.message("https://youtu.be/9kJqFfVISvs".format(room.name, user.name.title(), message.body))
        
    if cmd.lower() == "blunt" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/11/blunt.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "mid" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/12/mid.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "prrt" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/12/prrt.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "jackoff" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/01/jackoff.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "autoloud" and prfx:
      room.message("https://www.youtube.com/watch?v=CV4zte4FxkY".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "snek" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2019/12/hiss.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "f":
      room.message("https://bongstream.live/wp-content/uploads/2020/01/f.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "ron" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/02/ron.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "cig" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/02/cig.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "mom" and prfx:
      room.message("https://www.youtube.com/watch?v=h-h7ZpHur5A".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "poggers" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/03/pog.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "puggy" and prfx:
      room.message("https://i.imgur.com/94vTp1U.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "ankh" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/03/stream-down.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "poison" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/03/Capture.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "heroin" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/04/nod.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "assrape" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/04/non-stop-ass-rape.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "ihateniggers" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/05/nig-song.mp3".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "crippledog" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/05/meme.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "fuckher" and prfx:
      room.message("https://youtu.be/hysHkSjVWZM".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "dmx" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/06/mane-2-grave.jpg".format(room.name, user.name.title(), message.body))


    if cmd.lower() == "lol" and prfx:
      room.message("*lol* *lol* *lol*")
      room.message("*lol* *lol* *lol*")
      room.message("*lol* *lol* *lol*".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "cocaina" and prfx:
      room.message("https://youtu.be/vO1of77GS5g".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "yajewedit" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/06/yajewedit.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "lopez" and prfx:
      room.message("https://youtu.be/7vCD1Rp2Q84".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "milkies" and prfx:
      room.message("https://youtu.be/QLhqjZ_aI4k".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "letsgo" and prfx:
      room.message("https://youtu.be/lxojghdp3d0".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "vamos" and prfx:
      room.message("https://youtu.be/WWceRKDfse4".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "cotton" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/06/Cotton-maga-e1592933304572.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "fwm" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/06/Attach10455_20200629_154752.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "sam" and prfx:
      room.message("https://youtu.be/g969zMYfNOA".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "eatdick" and prfx:
      room.message("https://youtu.be/APH97ErhxRQ".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "spooky" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/07/spooky.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "muncher" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/07/mean-muncher.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "overdose" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/07/dailydose.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "nbomb" and prfx:
      room.message("https://youtu.be/Xtp0ZNAFg3Y".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "bongstream" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2021/11/l_1161.jpg".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "dab" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/08/dab.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "modelo" and prfx:
      room.message("https://youtu.be/x9LnR3unsXo".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "twu" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/09/twu.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "flamez" and prfx:
      room.message("Take your meds schizo".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "votar" and prfx:
      room.message("https://www.youtube.com/watch?v=X-ZwOfaTMBc".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "fag" and prfx:
      room.message("https://youtu.be/FUJaEllZ9Gc".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "friday" and prfx:
      room.message("https://youtu.be/2FRBHyGqszA".format(room.name, user.name.title(), message.body))
      
    if cmd.lower() == "trap" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2020/12/trap.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "pahmp" and prfx:
      room.message("https://youtu.be/uvCwbfFn1Y8".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "dumpit" and prfx:
      room.message("https://youtu.be/y28Diszaoo4".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "nigstomp" and prfx:
      room.message("https://i.gifer.com/4DZz.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "tweaker" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2021/06/tweakers.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "bongo" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2021/07/bongo-this.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "kneel" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2021/11/kneel.jpg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "manekwon" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2021/11/manekwon.png".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "labonga" and prfx:
      room.message("https://i.imgur.com/M8ohS4u.jpeg".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "eagles" and prfx:
      room.message("https://bongstream.live/wp-content/uploads/2022/01/eagles.gif".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "mc" and prfx:
      room.message("bongstream.apexmc.co (now in 1.18.2) 199.19.76.130:25706".format(room.name, user.name.title(), message.body))

    if cmd.lower() == "oldmc" and prfx:
      room.message("https://drive.google.com/file/d/1VdVWQkww5LU2ouLkKCEYPAhJ54H87gUy/view?usp=sharing".format(room.name, user.name.title(), message.body))

    ##WHOGAY
    if cmd.lower() == "whogay" and prfx:
      gay = random.choice(room.usernames)
      if gay == "bong":
        room.message("YOU NIGGA")
      elif gay == "negro":
        room.message("Next nigga dat type")
      else:
        room.message("@"+str(gay).replace("!","").replace("#","")+ " ur gay lol")

    randRoll = random.randint(1,10000)
    isDubs = randRoll % 100
    isTrips = randRoll % 1000

    ##CHEATING
    if message.body.startswith("!roll dubs"):
      if user.name in str(room.modnames) or user.name == room.ownername:
        cheat = str(random.randint(1,99)) + random.choice(cheaterdubs)
        room.message(cheat)
        room.message(random.choice(woo))
      else:
        room.message(str(randRoll))
    ##NORMAL ROLL
    elif cmd.lower() == "roll" and prfx:
      # Quads check
      if randRoll % 1111 == 0:
        room.message(str(randRoll))
        room.message(random.choice(checkEm))
        room.message(random.choice(checkEm))
        room.message(random.choice(checkEm))
      elif isTrips % 111 == 0:
        room.message(str(randRoll))
        room.message(random.choice(checkEm))
        room.message(random.choice(checkEm))
      elif isDubs % 11 == 0:
        room.message(str(randRoll))
        room.message(random.choice(checkEm))
      else:
        room.message(str(randRoll))

    if cmd.lower() == "random" and prfx:
      room.message(random.choice(commands))

    if cmd.lower() == "commands" and prfx:
      room.message(str(commands[0:]).replace("!",""))

    if cmd.lower() == "how2roulette" and prfx:
      room.message("ROULETTE SYNTAX EXAMPLES: !roulette followed by something like: \r\r50 on 15 / 10 on red / 20 on even black / 15 on odd / 5 on 6 9 12 15 19\r\rMULTI-BETS ARE INDIVIDUAL WAGERS e.g. '5 on 7 8 9 black' is a wager of 5 BongBux on 7, 8, 9, and black for a total stake of 20 BongBux.\r\r GO ALL IN OR YOU'RE A PUSSY")


##################################################################################
    ##SLOTS    
    if cmd.lower() == "slots" and prfx:
      spin = []
      
      ##GATEKEEP ANON
      if user.name.startswith("#") or user.name.startswith("!"):
        room.message("Register you broke ass nigga!")
      elif path.isfile(str(user.name)+".csv") == False:
        room.message("type !bongbux to get yuh first round of food stamps, on da house")
      ##CHECK FO BALANCE / MAKE FILE
      else:
        if path.isfile(str(user.name)+".csv") == True:
          buxFile = open(str(user.name)+".csv","r")
          for line in buxFile:
            balance = line
          if int(balance) <= 0:
            room.message("https://bongstream.live/wp-content/uploads/2020/11/brokeass.jpg")
            buxFile.close()
          else:
            buxFile.close()
            random.seed()
            slotFuck = random.randint(1,1000)
            for i in range (0,2):
              spin.append(random.choice(slot))
            if spin[0] == spin[1]:            
              if slotFuck >= 1 and slotFuck <= 50:
                spin.append("Jackpot")
              elif slotFuck >= 51 and slotFuck <= 200:
                spin.append("Mane")
              elif slotFuck >=201 and slotFuck <=500:
                spin.append("Ramen")
              elif slotFuck >=900 and slotFuck <=1000:
                spin.append("Nigger")
              else:
                spin.append("Weed")
            else:
              spin.append(random.choice(slot))
              
            if spin[0] == spin[1] and spin[0] == spin[2]:
              room.message(str(spin).replace("'","").replace(",","").replace("[[","[").replace("]]","]"))
              if str(spin[0]) == "Weed":
                room.message("https://thumbs.gfycat.com/FamousFabulousHerculesbeetle-size_restricted.gif")
                room.message(user.name+" won 420 BongBux!"+ "\r"+str(user.name)+ "'s account balance: " + str(int(balance)+420)+" BongBux")
                buxFile = open(str(user.name)+".csv","r")
                for line in buxFile:
                    balance = line     
                buxFile.close()
                balance = int(balance) + 420
                buxFile = open(str(user.name)+".csv","w")
                buxFile.write(str(balance))
                buxFile.close()

              if str(spin[0]) == "Nigger":
                room.message(random.choice(nigs))
                room.message(user.name+" Dis a muddafuggin stigup nigga gib me dem bongbux. I need abouta tree fiddy fo my nex fix"+ "\r"+str(user.name)+ "'s account balance: "+ str(int(balance)-350)+" BongBux")
                buxFile = open(str(user.name)+".csv","r")
                for line in buxFile:
                    balance = line     
                buxFile.close()
                balance = int(balance) - 350
                buxFile = open(str(user.name)+".csv","w")
                buxFile.write(str(balance))
                buxFile.close()

              if str(spin[0]) == "Mane":
                room.message("https://youtu.be/Ma0KmHILhzg")
                room.message(user.name+" won 305 BongBux!"+ "\r"+str(user.name)+ "'s account balance: "+ str(int(balance)+ 305)+" BongBux")
                buxFile = open(str(user.name)+".csv","r")
                for line in buxFile:
                    balance = line     
                buxFile.close()
                balance = int(balance) + 305
                buxFile = open(str(user.name)+".csv","w")
                buxFile.write(str(balance))
                buxFile.close()

              if str(spin[0]) == "Ramen":
                room.message("https://bongstream.live/wp-content/uploads/2021/03/ramen.jpg")
                room.message(user.name+" won 250 BongBux!"+ "\r"+str(user.name)+ "'s account balance: "+ str(int(balance)+ 250)+" BongBux")
                buxFile = open(str(user.name)+".csv","r")
                for line in buxFile:
                    balance = line     
                buxFile.close()
                balance = int(balance) + 250
                buxFile = open(str(user.name)+".csv","w")
                buxFile.write(str(balance))
                buxFile.close()

              if str(spin[0]) == "Jackpot":
                room.message("https://bongstream.live/wp-content/uploads/2019/12/jackpot.jpg SHIIIIIIIIIIETTTT")
                room.message(user.name+" won 6969 BongBux!"+ "\r"+str(user.name)+ "'s account balance: "+ str(int(balance)+6969)+" BongBux")
                buxFile = open(str(user.name)+".csv","r")
                for line in buxFile:
                    balance = line     
                buxFile.close()
                balance = int(balance) + 6969
                buxFile = open(str(user.name)+".csv","w")
                buxFile.write(str(balance))
                buxFile.close()
            else:
              room.message(str(spin).replace("'","").replace(",","").replace("[[","[").replace("]]","]") +
                           "\r"+str(user.name)+ "'s account balance: "+ str(int(balance)-5)+" BongBux")
              buxFile = open(str(user.name)+".csv","r")
              for line in buxFile:
                  balance = line     
              buxFile.close()
              balance = int(balance) - 5
              buxFile = open(str(user.name)+".csv","w")
              buxFile.write(str(balance))
              buxFile.close()
              
##################################################################################
              
    ##BONGBUX

    #ANON HANDLING
    if cmd.lower() == "bongbux" and prfx:
      if user.name.startswith("#") or user.name.startswith("!"):
        room.message("Register you broke ass nigga!")

    #IF NO FILE EXISTS
      elif path.isfile(str(user.name)+".csv") == False:
        buxFile = open(str(user.name)+".csv","w")
        buxFile.write("5000")
        buxFile.close()
        buxFile = open(str(user.name)+".csv","r")
        for line in buxFile:
          balance = line
        room.message(user.name + " has been blessed with xim/xer first " + str(balance).replace("[","").replace("]","").replace("'","") + " BongBux.")
        buxFile.close()

    #IF FILE EXISTS
      elif path.isfile(str(user.name)+".csv") == True:
        buxFile = open(str(user.name)+".csv","r")
        for line in buxFile:
          balance = line
        room.message(user.name + " has " + str(balance).replace("[","").replace("]","").replace("'","") + " BongBux.")

            
        buxFile.close()

##################################################################################


##ROULETTE

        ##CHECK FO BALANCE
    if cmd.lower() == "roulette" and prfx:
      if user.name.startswith("#") or user.name.startswith("!"):
        room.message("Register you broke ass nigga!")
      elif path.isfile(str(user.name)+".csv") == False:
        room.message("type !bongbux to get yuh first round of food stamps, on da house")
      else:
        if path.isfile(str(user.name)+".csv") == True:
          buxFile = open(str(user.name)+".csv","r")
          for line in buxFile:
            balance = line
          if int(balance) <= 0:
            room.message("You're broke nigga! Get yo ass some help 1-800-522-4700")
            buxFile.close()
          else:
            balance = int(balance)
            buxFile.close()
            ##BREAKDOWN COMMAND
            roulettePhrase = args.split(" ", 2)
            betAmount = int(roulettePhrase[0])
            betOn = roulettePhrase[1].lower()
            betTarget = roulettePhrase[2].lower()
            betDiv = betTarget.strip().split(" ")
            betDiv = set(betDiv)
            totalBet = int(betAmount*int(len(betDiv)))       

            '''
            ##DIAGNOSTICS
            print()
            print("DIAGNOSTICS:")
            print(roulettePhrase)
            print(betAmount)
            print(betOn)
            print(betTarget)
            '''
            
            ##VALIDATE BETS
            if validBets.issuperset(betDiv) == False or betAmount <=0:
              print("Nope that shit is broken.")
            else:

              '''
              ##VALIDATED BETS
              print(betDiv)
              print(len(betDiv))
              print()
              '''
                  
              ##IMMENSE VALIDATION
              if betOn != "on":
                print("ERROR")
              else:
                
                '''
                print("Account Balance:")
                print(balance)
                print("Bet Total:")
                print(totalBet)
                '''
                
                if totalBet > balance:
                  room.message("Insufficient food stamps.")
                else:
  
                  ##ACTUAL ROULETTE
                  spinResult = random.choice(validSpin)
                  if spinResult == "0" or spinResult == "00":
                    spinColor = "green"
                    spinParity = "neither"
                  elif int(spinResult)%2 > 0:
                    spinParity = "odd"
                  else:
                    spinParity = "even"

                  if spinResult in redSpin:
                    spinColor = "red"

                  if spinResult in blackSpin:
                    spinColor = "black"

                  ##CALCULATIONS
                  spinSet = {spinResult,spinColor,spinParity}
                  spinCommon = betDiv.intersection(spinSet)
                  spinWrong = betDiv.difference(spinSet)
                  betDeduction = (int(betAmount) * len(spinWrong))

                  spinSingles = set(validSpin).intersection(spinCommon)
                  spinOthers = set(validOthers).intersection(spinCommon)
                  singlesWinnings = (int(betAmount) * 35 * len(spinSingles))
                  othersWinnings = (int(betAmount) * 1 * len(spinOthers))
                  betWinnings = singlesWinnings + othersWinnings 
                  betNetChange = (betWinnings - betDeduction)
                  balance = balance + betNetChange

                  buxFile = open(str(user.name)+".csv","w")
                  buxFile.write(str(balance))
                  buxFile.close()

                  ##RESULTS
                  '''
                  print("Matches:")
                  print(spinCommon)
                  print(spinSingles)
                  print(spinOthers)
                  
                  print("Winnings:")
                  print(singlesWinnings)
                  print(othersWinnings)
                  print("Wrong:")
                  print(spinWrong)
                  print("Losings:")
                  print(betDeduction)
                  print("New balance:")
                  print(balance)
                  '''
                  
                  
                  room.message(spinResult + " (" + spinColor.upper() + ", " + spinParity.upper()+")" +"\r" +
                               (str(user.name) + "'s net winnings = " + str(betNetChange) +
                                " BongBux.\r"+ str(user.name) + "'s account balance: " + str(balance) +" BongBux."))

                  

                  
                  
                  

        






rooms = ["bongstream", "chadstream"]
username = "bongbot"
password = "fucku12"

bot.easy_start(rooms,username,password)

##bonglord69:usuk1210
##bongbot : fucku12
##NEGRO : Fuckyoubong1
##mane213 : fuckxans1210

## ALL PW niggerlover42
## evil : Aryan : Bastard : Willcommitmurder1day : Geo : nasi
