import discord
import asyncio
import os


from os import listdir
from random import *
from discord.ext.commands import Bot, Context

bot = Bot(command_prefix=',')

ex = '1. 好：音ㄏㄠˋ/hào，愛好、嗜好。&2. 食以草具：即「以草具食之」，拿粗劣的食物給他吃。食，音ㄙˋ/sì，施食與人。草具，粗劣的飲食。&3. 鋏：音ㄐㄧㄚˊ/jiá，劍柄，這裡指劍。&4. 過：拜訪。&5. 客我：以尊客之禮待我。客，此作動詞用。&6. 出記：發出布告。記，文告。&7. 習計會：熟習會計。計會，即會計。會，音ㄎㄨㄞˋ/kuài。&8. 責：音ㄓㄞˋ/zhài，通「債」，債款。&9. 署：音ㄕㄨˋ/shù，簽名。&10. 謝：道歉。&11. 憒於憂：因憂慮而心煩意亂。憒，音ㄎㄨㄟˋ/kuì，昏亂、糊塗。&12. 懧愚：懦弱愚昧。懧，音ㄋㄨㄛˋ/nuò，同「懦」。&13. 約車治裝：準備車輛，整理行裝。約，束，引申為整束、整理。&14. 券契：指債券契據。券，音ㄑㄩㄢˋ/quàn，契據。&15. 矯命：假傳孟嘗君的命令。矯，音ㄐㄧㄠˇ/jiǎo，假託、詐稱。&16. 長驅：一路趕車，不加停留。&17. 衣冠而見之：穿好衣服、戴上帽子來接見他，表示禮敬之意。衣、冠，音ㄧˋ /yì、ㄍㄨㄢˋ/guàn，均作動詞用。&18. 區區：小小，形容微不足道。&19. 不拊愛子其民：不安撫愛護人民，不視民如子。拊，音ㄈㄨˇ/fǔ，通「撫」，安撫。子，此作動詞，謂視民如子。&20. 賈利之：在百姓身上謀取利益。賈，音ㄍㄨˇ/gǔ，買賣、做生意，在此有求取之意。&21. 朞年：此指一週年。朞，音ㄐㄧ/jī，同「期」，循環回復，有週期之意。&22. 窟：音ㄎㄨ/kū，洞穴。&23. 虛上位：空出高位。虛，這裡作動詞用，空出。上位，這裡指相位。&24. 先驅：先驅車趕回。&25賫：音ㄐㄧ/jī，通「齎」，贈送。&27不足為：不值得幫助。為，音ㄨㄟˋ/wèi，幫助。&28. 纖介：猶言細微、微小。纖，細絲，引申為細微。介，通「 芥」 ，小草，引申為微小。&1.竊以為過：我私下認為這是錯的。竊，謙詞。&2.舉地：攻取土地。舉，拔，攻下。&3.膏腴之壤：肥沃的土地。膏，肥油。腴，音ㄩˊ，腹下肥肉。&4.施：音ㄧˋ，延續。&5.彊公室杜私門：增強王室的權力，杜絕權貴的私人勢力。杜，杜絕。私門，私家，相對於「公室」，此指穰侯、華陽君等豪門貴族的私人勢力。&6.蠶食諸侯：像蠶啃桑葉般，逐步併吞諸侯。&7.向使：假使。&8.卻客而不內： 拒絕賓客，不予接納。卻，拒絕。內，通「納」，音ㄋㄚˋ。&9.隨俗雅化： 隨時應俗而高雅合宜。指打扮時髦，應對合宜。&10.佳冶窈窕 ：容貌美豔，體態美好。窈窕，形容女子體態優雅美好的樣子。&11.擊甕叩缶： 敲擊陶器、瓦器作樂。叩，擊。缶，音ㄈㄡˇ，瓦器。甕、缶為秦國陶製打擊樂器，聲音粗獷、質樸。&12.彈箏搏髀： 彈著箏，拍大腿。搏，拍打。髀，音ㄅㄧˋ，大腿。&13.適觀： 適合觀賞。&14.可否： 此指才能的優劣。&15.跨： 占據、據有。&16.讓： 推辭、捨棄。&17.棄黔首以資敵國： 捨棄百姓來幫助敵國。黔首，百姓。黔，音ㄑㄧㄢˊ，黑色。資，資助、供給。&18.裹足： 纏裹其足，引申為止足不前。&19.藉寇兵而齎盜糧： 借給敵寇兵器，供給盜賊糧食。藉，通「借」。齎，音ㄐㄧ，贈送、給予。&20.損民以益讎： 減少自己國家人民而增加仇人的力量。讎，音ㄔㄡˊ，同「仇」。&1. 濠梁：濠水的橋上。莊子和惠子在此處辯論人是否能感知魚的快樂；莊子說自己能，惠子認為不能。梁，橋。&2. 鯈魚：一種銀白色的小魚。鯈，音ㄔㄡˊ/chóu。&3. 以己度人：用自己的猜測來推想別人的心意。度，音ㄉㄨㄛˋ/duò，考慮、推測。&4. 脾氣：此指人的習性。&5. 外射：人將內心的感受或想法加諸外物，且視之為物本有的特性，此為美學用語。&6. 作如是觀：這個角度或以這個態度看某件事物。&7. 儕輩：同輩。儕，音ㄔㄞˊ/chái。&8. 勁節：堅毅不屈的節操。&9. 暗香疏影：形容梅花的幽香及其橫斜的枝幹。後為梅花的代稱。語出林逋　山園小梅。&10. 高標：指高尚的人格。&11. 清風亮節：指高尚的品格和堅貞的氣節。&12. 物我同一：客觀事物與主觀的情感融合一致。&13. 宏纖：大小粗細，此指節奏的輕重。&14. 人情：指人與生俱來的喜怒哀樂等感情。&15. 抑鬱悽惻：鬱悶悲傷。&16. 骨力：書法的筆力。&17. 展頤：微笑。頤，音ㄧˊ/yí，鼻子兩側腮頰部分。&18. 泅水：游泳。泅，音ㄑㄧㄡˊ/qiú。&1.本土意識：此指強調臺灣在地歷史文化與主體意識的一種思想主張。&2.平地山胞：今稱平地原住民。指臺灣光復前，設籍於平地行政區內的原住民；倘原籍在山地行政區內，則稱「山地山胞」。&3.頭目：由部落長老會議公推產生的政治與軍事首領，負責協調部落重大事務，也是早期獵首、征戰的領導人物。&4.會所制度：卑南族男子依照年齡階級，進行階段性教育訓練的社會制度。「會所」也稱「集會所」，可分為少年會所與青年會所二階級。&5.祭司：掌管與主持部落的農耕祭儀。&6.宿於妻家：卑南族為母系氏族社會，實行男子入婚制的習俗。&7.祖靈屋：為各家族祭祀祖宗之靈的小屋，其功能與意涵近似漢民族的宗祠或家廟。&8.笞臀：鞭打臀部的儀式，除了象徵建立領導權威，要求成員遵守法規戒律之外，也訓練個人的忍耐力。笞，音ㄔ/chī，用鞭或竹板打(例如：鞭笞)。&9.禳災祛邪：此指通過猴祭儀式解除災難去除邪惡之氣。禳，音ㄖㄤˊ/ráng，祭神祈求消除災變。祛，音ㄑㄩ/qū&1.要衝：多條重要道路會合的地方，此處指關鍵地位。&2.躡手躡足：放輕手腳走路，行動小心翼翼，不敢聲張的樣子。躡，音ㄋㄧㄝˋ/niè。&3.開門揖盜：打開門，邀請盜徒入內。揖，音ㄧ，拱手行禮。&4.囁嚅：音ㄋㄧㄝˋ ㄖㄨˊ/niè rú，有話想說又不敢說，吞吞吐吐的樣子。&5.大言不慚：不顧事實、妄言誇大而不知羞慚。&6.惴惴不安：因恐懼耽憂而心神不定。惴，音ㄓㄨㄟˋ/zhuì。&7.殺機陡萌：殺害對方的念頭突然萌生。&8.調羹：湯匙。&9.僭越：超越本分行事。&10.二人同心其利斷金：二人同心協力，力量如同鋒利的刀劍，可以切斷金屬。謂團結的力量可以對付敵人。語出易經 繫辭上。&11.或然率：以數值表現事物發生的可能性。也稱為「機率」。&12.嚴夷夏之防：堅持華夏民族與異族的界限，避免夷人的風俗改變了華 夏文化。夷，古代對中原以外各族的稱呼。&13.鍥而不舍：比喻堅持到底，奮勉不懈。鍥，音ㄑㄧㄝˋ/qiè，鏤刻。舍，捨棄、停止。&14.秦晉：春秋時代，秦、晉二國世代多互為婚嫁。後遂以秦 晉代指婚姻關係(例如：秦晉之好)。&15.迂闊：思想言行不合實際。迂，言行誇誕、不切實際。闊，不切實際。&1. 盤纏：旅費。纏，音ㄔㄢˊ/chán。&2. 迤邐：音一ˇ ㄌ一ˇ/yǐ lǐ，連續不斷，此指旅程蜿蜒曲折。&3. 刺配：古代在罪犯臉上刺字，並發配遠方充軍。&4. 玷辱：污辱。玷，音ㄉ一ㄢˋ/diàn。&5. 渾家：妻子。&6. 閃將進來(第二段)：閃了進來。將：語助詞，相當於「了」。&7. 官人：具官位或有地位者。&8. 那個人「將」出一兩銀子(第二段)：動詞，拿。&9. 這兩個人來得「不尷尬」(第三段)：行為鬼祟，神色有異，又作「尷尬」ㄍㄢ ㄍㄚˋ/gān gà。&10.不省得：不了解。省：此處唸作ㄒㄧㄥˇ/xǐng。&11.一個時辰：兩個小時。&12.好歹要「結果」他性命：將人殺死。&13.彤雲密布：紅色雲彩。彤，音ㄊㄨㄥˊ/tóng，赤紅色的。&14.朔風：北方吹來的寒風。朔：ㄕㄨㄛˋ/shuò。&15.出來把草廳門「拽上」(第七段)：拉上。拽，音，ㄓㄨㄞˋ/zhuài。&16.接風：設宴款待遠來或歸來的親友。&17.懷裡「揣」了牛肉(第八段)：塞進。揣，音，ㄔㄨㄞˇ/chuǎi。&18.旁邊只有一塊大石頭，「掇將」過來(第九段)：搬了。掇，音ㄉㄨㄛˊ/duó。&19.張教頭那「廝」(第十段)：輕侮不敬的稱呼。&20.央浼：請求。浼：ㄇㄟˇ/měi。&21.這「早晚」燒個八分過了(第十段)：時候。&22.天可憐見：承蒙上天垂憐庇佑。&23.林沖舉手，肐察一聲，先「搠」倒差撥(第十一段)：音ㄕㄨㄛˋ/shuò，刺。&24.冤讎：仇恨。讎，音ㄔㄡˊ/chóu。&25.把尖刀向心窩裡只一「剜」：音ㄨㄢ/wān，用刀挖取'
sens = ex.split('&')

for filename in listdir('cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'cog.{filename[:-3]}')
        print(f'Cog {filename}을/를 가져왔습니다')

@bot.event
async def on_ready():
    
    print(bot.user.name)
    print('봇이 시작됨')
    game = discord.Game('.a 로 도움말을 확인해보세요')
    await bot.change_presence(status=discord.Status.online, activity=game)
    
@bot.event
async def on_message(message: str):
    if message.author.bot: 
        return None 

    if message.content.startswith('.'):
        letter = str(message.content)[1]
        
        has = False
        for i in range(0, len(sens)):
            words = sens[i].split('：')
            if(letter in words[0]):
                has = True
                await message.channel.send(f"{sens[i]}")
        
        if(has == False):
            await message.channel.send("없음")
        
        
            
            
    


#
bot.run(os.environ['bot_token'])


