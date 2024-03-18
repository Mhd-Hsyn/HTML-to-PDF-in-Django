"""
useable.py
"""


def generate_pdf_summary(data):

    try:
        css= """
            <style type="text/css">
            .text {
                color: #b17d41;
            }

            .w-10 {
                text-align: center;
                margin-top: 5%;
                margin-bottom: 3%;
            }

            .w-20 {
                text-align: center;
                margin-top: 10%;
            }

            .p-font-size {
                font-size: 24px;
            }

            .row {
                display: contents;
            }

            .pfbg {
                background: #22272E;
            }

            .w-100 {
                width: 100%;
            }

            .blue {
                color: #118ab2;
            }

            .darkblue {
                color: #073b4c;
            }

            .orange {
                color: #ffd166;
            }
            .second-fontfamily{
                text-align: center;
                padding-right: 30px;


            }
        </style>
        
        """
                

        html_content= f"""

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PDF</title>
        </head>
        <body>

        {css}

        <page backtop="44mm" backbottom="18mm" backleft="10mm" backright="10mm" orientation="P" backimg="pdf-images/backgrounds.png" backimgx="1.5mm"
            backimgh="10mm" backimgw="100%">
            <page_header>
                <table class="page_header" cellpadding="12" cellspacing="0">
                    <tr>
                        <td class="blue" style="width: 100%; text-align:center; font-size: 50px; font-weight:bold; padding: 20px; text-transform: uppercase">{data['author_name']}'s Family</td>
                    </tr>
                    <tr>
                        <td class="blue" style="width: 100%; text-align:center; font-size: 50px; text-decoration: underline;"> Handbook Summary</td>
                    </tr>
                </table>
            </page_header>
            <page_footer>
                <!-- <b>
                    [[page_cu]]
                </b> -->
                <table class="page_footer row pfbg" cellpadding="12" cellspacing="0">
                    <tr>
                        <td style="width: 50%; color: #fff; font-size: 18px;padding: 10px auto 10px 10px;"> The {data['author_name']} Family Handbook</td>
                        <td style="width: 10%; color: #fff; font-size: 18px;padding: 10px 10px 10px auto;">[[page_cu]]</td>
                        <td style="width: 10%"></td>
                        <td style="width: 30%; color: #fff; font-size: 18px;padding: 10px 10px 10px 10px;">
                            <!-- Create Your Family Logo -->
                        </td>
                    </tr>
                </table>
            </page_footer>
        </page>

        <div class="section">
            <table style="width: 100%; margin-top: 20px;" class="row w-100" cellpadding="12" cellspacing="14">
                <tr>
                    <td class="second-fontfamily black" style="width: 40%; font-weight: bold; font-size:20px; padding-top: 75px; ">Author/Authors:<br><p class="blue" style="margin-top: 10px;">{data['author_name']}</p></td>
                    <td style="width: 20%;">
                    </td>
                    <td class="second-fontfamily black" style="width: 40%; font-weight: bold; font-size:20px; padding-top: 75px; ">Author Address:<br><p class="blue" style="margin-top: 10px; text-align:center">{data['author_address']}</p></td>
                </tr>
                <tr>
                    <td class="third-fontfamily darkblue" style="width: 40%;"></td>
                    <td style="width: 20%;"></td>
                    <td class="third-fontfamily darkblue" style="width: 40%;"></td>
                </tr>
                <tr>
                    <td colspan="3">&nbsp;</td>
                </tr>
            </table>

            <p class='darkblue' style='font-size:24px;color:#073b4c;margin-top:10px'>This is a sample note.</p>
        </div>

        </page>
        </body>
        </html>

        """


        return {"status": True, "pdf_code": html_content}

    except Exception as e :
        print(e)
        return {"status":False}
    

def generate_pdf_familybios(data):
    try:
        css= """

        <style type="text/css">
            .text {
                color: #b17d41;
            }

            .w-10 {
                text-align: center;
                margin-top: 5%;
                margin-bottom: 3%;
            }

            .w-20 {
                text-align: center;
                margin-top: 10%;
            }

            .p-font-size {
                font-size: 28px;
            }

            .row {
                display: contents;
            }

            .pfbg {
                background: #22272E;
            }

            .w-100 {
                width: 100%;
            }

            .blue {
                color: #118ab2;
            }

            .darkblue {
                color: #073b4c;
            }

            .bluenew {
                color: #175f87;
            }

            .orange {
                color: #ffd166;
            }

        </style>

        """


        html= f"""

        {css}

        <page backtop="7mm" backbottom="10mm" backleft="10mm" orientation="P" backright="10mm"
            backimg="{{ public_path('pdf-images/backgrounds.png') }}" backimgx="1.5mm" backimgh="10mm" backimgw="100%"
            style="font-family:times, serif">
            <page_header>
            </page_header>
            <page_footer>
                <table class="page_footer row pfbg" cellpadding="12" cellspacing="0">
                    <tr>
                        <td style="width: 50%; color: #fff; font-size: 18px;padding: 10px auto 10px 10px;"> The
                            {data['lname']} Family Handbook</td>
                        <td style="width: 10%; color: #fff; font-size: 18px;padding: 10px 10px 10px auto;">[[page_cu]]</td>
                        <td style="width: 10%"></td>
                        <td style="width: 30%; color: #fff; font-size: 18px;padding: 10px 10px 10px 10px;"></td>
                    </tr>
                </table>
            </page_footer>
            <table class="row w-100" cellpadding="12" cellspacing="0">
                <tr>
                    <td style="width: 100%; text-align: center;">
                        <h1 style="font-weight: bold; font-size: 100px;">The</h1>
                    </td>
                </tr>
                <tr>
                    <td class="bluenew" style="width: 100%; text-align: center; font-weight: bold; font-size: 50px;">
                        {data['lname']}</td>
                </tr>
                <tr>
                    <td style="width: 100%; font-weight: 100; font-size: 50px; text-align: center;">Family Members</td>
                </tr>
            </table>
            
                <div>
                    <table style="margin-top: 30px" class="row w-100" cellpadding="12" cellspacing="0">
                        <tr>
                            <td class="blue" style="width: 20%;font-size: 18px;"></td>
                            <td colspan="3" class="blue"
                                style="width: 100%; padding: 5px; font-size: 35px;font-weight: bold;">
                                {data['relation_name']}
                            </td>
                        </tr>
                        <tr>

                            <td class="blue" rowspan="3" style="width: 10%;">
                                
                                    <div
                                        style="border:3px solid; width:150px; height: 150px; border-radius: 75px; background-image: url({{ public_path('storage/' . $parent_member['image']) }}); background-repeat: no-repeat; background-position: center;">
                                    </div>
                                    <div style="border:3px solid; width:100px;">
                                        <img src="{{ public_path('storage/'.$parent_member['image']) }}" height="100" width="100" alt="">
                                    </div>
                                
                            </td>
                            <td class="blue" style="width: 20%;font-size: 18px;text-align: {{ $direction }}">
                                <span style="font-weight: bold;">Family Role:</span> <br> <span
                                    style="color: #000;"> {data['relation']}
                                </span>
                            </td>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;"> Birthday: </span> <br> <span
                                    style="color: #000;">{data['relation_dob']}</span>
                            </td>
                        </tr>
                        <tr>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">Lives In:</span> <br> <span
                                    style="color: #000;">{data['relation_livesin']}</span>
                            </td>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">Birth Place :</span> <br> <span
                                    style="color: #000;">{data['relation_pob']}</span>
                            </td>
                        </tr>
                        <tr>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">Favorite Food:</span> <br> <span
                                    style="color: #000;">{data['relation_fav_food']}</span>
                            </td>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">My Profession:</span> <br> <span
                                    style="color: #000;">{data['relation_profession']}</span>
                            </td>
                        </tr>
                        <tr>
                            <td class="blue" rowspan="3" style="width: 10%;"></td>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">Favorite Holiday:</span> <br> <span
                                    style="color: #000;">{data['relation_fav_holiday']}</span>
                            </td>
                            <td class="blue" style="width: 20%;font-size: 18px;">
                                <span style="font-weight: bold;">Greatest Fear:</span> <br>
                                <span
                                    style="color: #000;text-left">{data['relation_fear']}</span>
                            </td>
                        </tr>
                    </table>
                    <table class="row w-100" cellpadding="12" cellspacing="0">
                        <tr>
                            <td style="width: 10%;"></td>
                            <td class="blue" style="width: 60%;font-size: 18px;"> <br>
                                <span style="font-size: 18px;color:#000;"> {data['relation_fav_qoute']} </span>
                            </td>
                        </tr>
                        <tr>
                            <td class="blue" style="width: 20%; padding-left: 15px;">
                                
                                    <div style="border:3px solid; width:100px;">
                                        <img src="{data['relation_img']}" height="100"
                                            width="100" alt="">
                                    </div>
                            </td>
                        </tr>
                    </table>
                    <hr>
                </div>
            <div>
            

        """
        return {"status": True, "pdf_code": html}

    except Exception as e :
        print(e)
        return {"status":False}