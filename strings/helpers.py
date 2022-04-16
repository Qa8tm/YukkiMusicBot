#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>اوامر الادمن:</u>**

ايقاف - لايقاف الاغاني.
استئناف - لاستمرار الفيديو.
كتم - لكتم الاغنية.
الغاء كتم - لالغاء كتم الاغنية.
تخطي - لتخطي الاغنية الحاليه.
خلط - تشغيل من قائمة عشوائيا.
اعادة تشغيل - لاعادة  تشغيل البوت.


✅<u>**تخطي مميز:**</u>
تخطي [رقم(مثال: 3)] 
    - لتخطي عدد من الاغاني في مرة واحدة.

✅<u>**التكرار:**</u>
تكرار [تفعيل/تعطيل] او [عدد بين 1-10] 
    - عند التفعيل يتم تشغيل الاغنية تلقائيا 10 مرات.

✅<u>**اوامر الادمن:**</u>
للوثوق من شخص ليمكنه استعمال اوامر البوت.

رفع [يوزر] - اضافه شخص للادمنية
تنزيل [يوزر] - حذف شخص من الادمنية.
الادمنية - تحصص من ادمنية الكروب"""


HELP_2 = """✅<u>**اوامر التشغيل:**</u>

تشغيل  - لتشغيل الاغاني في الاتصال في الكروبات والقنوات.

ق تشغيل [يوزر القناة او الايدي] او [تعطيل] - لربط قناة للتشغيل في البوت.


✅**<u>اوامر القوائم:</u>**
قائمة  - فحص القوائم التشغيل.
حذف قائمة - لحذف قائمة تشغيل
تشغيل قائمة  - لتشغيل القوائم."""


HELP_3 = """✅<u>**اوامر البوت:**</u>

الاحصائيات - احصل على افضل 10 اغاني في البوت تم تشغيلها.

الادمنية - رؤية الادمنية في بوت ميوزك جيبثون

الكلمات [اسم الاغنية] - للبحث عن كلمات الاغنية في الكوكل.

تحميل [اسم الاغنية] او [رابط يوتيوب] - تحميل اي اغنية.

انتظر- لوضع اغنية في الانتظار."""

HELP_4 = """✅<u>**الاوامر الاساسية:**</u>
فحص - تشغيل البوت.
الاوامر  - للحصول على قائمة الاوامر.
بنك - للحصول على سرعة البوت

✅<u>**اوامر الكروب:**</u>
الاعدادات -احصل على إعدادات المجموعة الكاملة باستخدام الأزرار المضمنة

🔗 ** الخيارات في الإعدادات:**

1️⃣ يمكنك ضبط ** جودة الصوت ** التي تريد بثها على الدردشة الصوتية.

2️⃣ يمكنك ضبط ** جودة الفيديو ** التي تريد بثها على الدردشة الصوتية.

3️⃣ ** المستخدمون المصدقون **: - يمكنك تغيير وضع أوامر المسؤول من هنا للجميع أو للمسؤولين فقط. إذا كان كل شخص موجودًا في مجموعتك ، فسيكون قادرًا على استخدام أوامر المسؤول(مثل تخطي, انهاء وغيرها)

4️⃣ ** الوضع النظيف: ** عند التمكين ، يحذف رسائل الروبوت بعد 5 دقائق من مجموعتك للتأكد من بقاء محادثتك نظيفة وجيدة.

5️⃣ **امر التنظيف** : عند التفعيل البوت سيحذف الاوامر مثل  (تشغيل, ايقاف, خلط, انهاء وغيرها) .

6️⃣ **اوامر التشغيل:**

وضع التشغيل - احصل على لوحة إعدادات تشغيل كاملة مع أزرار حيث يمكنك ضبط إعدادات تشغيل مجموعتك.

<u>خيارات في وضع التشغيل:</u>

1️⃣ **وضع البحث ** [مباشر أو مضمن] - يغير وضع البحث أثناء التشغيل (تشغيل). 

2️⃣ **اوامر الادمن** [للكل او للادمن فقط] - إذا كان كل شخص موجودًا في مجموعتك ، فسيكون قادرًا على استخدام أوامر المسؤول(مثل تخطي, انهاء etc)

3️⃣ **نوع التشغيل** [للكل او للادمن] - إذا كان المسؤولون ، فيمكن للمسؤولين الموجودين في المجموعة فقط تشغيل الموسيقى على الدردشة الصوتية."""

HELP_5 = """🔰**<u>اضافه وحذف ادمن :</u>**
رفع [يوزر او بالرد]
تنزيل [يوزر او بالرد]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
تحديثث - Reboot your Bot. 
تحديث - Update Bot.
سرعة البوت - فحص سرعة البوت
صيانة [نفعيل / تعطيل] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.

📈**<u>اوامر الاحصائيات:</u>**
الصوت المسغل - رؤية الاغنية الشغالة.
الفيديو المشغل - رؤية الفيديو الشغال
الاحصائيات - فحص حالة البوت

⚠️**<u>الكروبات المحظورة:</u>**
المحظور [ايدي] - قائمة المحظورين من البوت
الغير محظور [ايدي] - قائمة الغير محضورين من البوت

👤**<u>BLOCKED FUNCTION:</u>**
حظر [Username or Reply to a user] - Prevents a user from using bot commands.
الغاء حظر [Username or Reply to a user] - Remove a user from Bot's Blocked List.
المحظورين - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
تحميل [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.


"""
