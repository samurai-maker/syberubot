# Copyright (C) 2021 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# PLease read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

FROM cyberuserbot/cyberspaceaz:latest
RUN git clone https://github.com/samurai-maker/syberubot /root/CyberUserBot
WORKDIR /root/CyberUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
