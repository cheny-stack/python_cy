:: 目标路径 C:\work\montnets\twise-packges
:: 落地页
cd C:\work\montnets\5g-ccc-twise\web-landing-page
call npm install
call npm run build
7z a twise-5g-ccc-landing-page-front.zip ./dist
echo "twise-5g-ccc-landing-page-front.zip"
:: 复制到 C:\work\montnets\twise-packges
xcopy twise-5g-ccc-landing-page-front.zip C:\work\montnets\twise-packges\ /y

:: twise-5g-ccc
cd C:\work\montnets\5g-ccc-twise\web
call npm install
call npm run build
7z a twise-5g-ccc-front.zip ./dist
echo "twise-5g-ccc-front.zip"
:: 复制到 C:\work\montnets\twise-packges
xcopy twise-5g-ccc-front.zip C:\work\montnets\twise-packges\ /y

:: 5g-ccc-console
cd C:\work\montnets\5g-ccc\web
call npm install
call npm run build
7z a 5g-ccc-console-front.zip ./dist
echo "5g-ccc-console-front.zip"
:: 复制到 C:\work\montnets\twise-packges
xcopy 5g-ccc-console-front.zip C:\work\montnets\twise-packges\ /y



:: 5g-aim
cd C:\work\montnets\5g-aim\web-ec
call npm install
call npm run build
7z a 5g-aim-ec-front.zip ./dist
echo "5g-aim-ec-front.zip"
:: 复制到 C:\work\montnets\twise-packges
xcopy 5g-aim-ec-front.zip C:\work\montnets\twise-packges\ /y


:: 5g-aim-editor
cd C:\work\montnets\5g-aim\web-editor
call npm install
call npm run build
7z a 5g-aim-editor-front.zip ./dist
echo "5g-aim-ec-front.zip"
:: 复制到 C:\work\montnets\twise-packges
xcopy 5g-aim-editor-front.zip C:\work\montnets\twise-packges\ /y

