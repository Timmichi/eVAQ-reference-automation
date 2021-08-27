def format_html(tup, sender, date):
  return f'''
  <html
    xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office"
    xmlns:w="urn:schemas-microsoft-com:office:word"
    xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
    xmlns="http://www.w3.org/TR/REC-html40"
  >
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=us-ascii" />
      <meta name="Generator" content="Microsoft Word 15 (filtered medium)" />
      <style>
        <!--
            /* Font Definitions */
            @font-face
                {{font-family:"Cambria Math";
                panose-1:2 4 5 3 5 4 6 3 2 4;}}
            @font-face
                {{font-family:DengXian;
                panose-1:2 1 6 0 3 1 1 1 1 1;}}
            @font-face
                {{font-family:Calibri;
                panose-1:2 15 5 2 2 2 4 3 2 4;}}
            @font-face
                {{font-family:"Century Gothic";
                panose-1:2 11 5 2 2 2 2 2 2 4;}}
            @font-face
                {{font-family:"\@DengXian";
                panose-1:2 1 6 0 3 1 1 1 1 1;}}
            /* Style Definitions */
            p.MsoNormal, li.MsoNormal, div.MsoNormal
                {{margin:0in;
                font-size:11.0pt;
                font-family:"Calibri",sans-serif;}}
            a:link, span.MsoHyperlink
                {{mso-style-priority:99;
                color:#0563C1;
                text-decoration:underline;}}
            span.EmailStyle17
                {{mso-style-type:personal-compose;
                font-family:"Calibri",sans-serif;
                color:windowtext;}}
            .MsoChpDefault
                {{mso-style-type:export-only;}}
            @page WordSection1
                {{size:8.5in 11.0in;
                margin:1.0in 1.0in 1.0in 1.0in;}}
            div.WordSection1
                {{page:WordSection1;}}
            -->
      </style>
      <!--[if gte mso 9
        ]><xml> <o:shapedefaults v:ext="edit" spidmax="1026" /> </xml
      ><![endif]-->
      <!--[if gte mso 9
        ]><xml>
          <o:shapelayout v:ext="edit">
            <o:idmap v:ext="edit" data="1" /> </o:shapelayout></xml
      ><![endif]-->
    </head>
    <body
      lang="EN-US"
      link="#0563C1"
      vlink="#954F72"
      style="word-wrap: break-word"
    >
      <p>Hi {tup.name},</p>
      <p>
        I am {sender} from the California Department of Technology (CDT).
        I am contacting you for a reference check for {tup.vendor_name}, because
        this vendor has listed you as a reference for their eVAQ application with
        CDT. I have attached a one-page questionnaire for your review and comment.
        Could you please provide your answers to me so that I may have your
        reference on file for this vendor?
      </p>
      <p>
        At the top of the attached questionnaire is {tup.vendor_name}’s
        information that they provided for their contract with your organization.
        Question #1 is a verification that all of this information is correct
        which would give them a Pass rating. If this information were incorrect,
        then they would receive a Fail rating. The next 6 questions are explained
        in the attachment. If you could return this questionnaire to me by {date},
        it would be greatly appreciated. Please let me know if you have any
        questions regarding this matter.
      </p>
      <div class="WordSection1">
        <p class="MsoNormal"><o:p>&nbsp;</o:p></p>
        <table
          class="MsoNormalTable"
          border="0"
          cellspacing="3"
          cellpadding="0"
          width="446"
          style="width: 334.5pt"
        >
          <tr style="height: 86.65pt">
            <td style="padding: 0in 0in 0in 0in; height: 86.65pt">
              <p class="MsoNormal">
                <a href="http://www.cdt.ca.gov/" target="_blank"
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: blue;
                      text-decoration: none;
                    "
                    ><img
                      border="0"
                      width="100"
                      height="97"
                      style="width: 1.0416in; height: 1.0104in"
                      id="_x0000_i1025"
                      src="cid:logo_img"
                      alt="California Department of Technology" /></span></a
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><o:p></o:p
                ></span>
              </p>
            </td>
            <td style="padding: 0in 0in 0in 0in; height: 86.65pt">
              <p class="MsoNormal">
                <span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><img
                    border="0"
                    width="11"
                    height="141"
                    style="width: 0.1145in; height: 1.4687in"
                    id="_x0000_i1026"
                    src="cid:line_img"
                    alt="http://marketing.otech.ca.gov/signatures/line2.png" /><o:p></o:p
                ></span>
              </p>
            </td>
            <td
              width="302"
              style="width: 226.5pt; padding: 0in 0in 0in 0in; height: 86.65pt"
            >
              <p class="MsoNormal">
                <b
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: #1b4675;
                    "
                    >Timothy Simanhadi</span
                  ></b
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><br /></span
                ><span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                    color: #009ecc;
                  "
                  >Student Assistant <br /></span
                ><span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                    color: #1b4675;
                  "
                  >Statewide Technology Procurement (STP)<br /><o:p></o:p
                ></span>
                <span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                    color: #1b4675;
                  "
                  >CA Department of Technology&nbsp;(CDT)<br /></span
                ><span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><span style="color: #009ecc"
                    >916-431-4244 (Desk) 916-826-5334 (Cell)<o:p></o:p></span
                ></span><br />
                <span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                    color: #1f4e79;
                  "
                  >Email: <a href="mailto:timothy.simanhadi@state.ca.gov"
                    >timothy.simanhadi@state.ca.gov</a
                  ></span
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><br /></span
                ><a href="https://www.facebook.com/CADeptTech"
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: blue;
                      text-decoration: none;
                    "
                    ><img
                      border="0"
                      width="32"
                      height="32"
                      style="width: 0.3333in; height: 0.3333in"
                      id="_x0000_i1027"
                      src="cid:facebook_img"
                      alt="Facebook" /></span></a
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  >&nbsp;</span
                ><a href="https://twitter.com/CADeptTech" target="_blank"
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: blue;
                      text-decoration: none;
                    "
                    ><img
                      border="0"
                      width="32"
                      height="32"
                      style="width: 0.3333in; height: 0.3333in"
                      id="_x0000_i1028"
                      src="cid:twitter_img"
                      alt="Twitter" /></span></a
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  >&nbsp;</span
                ><a
                  href="https://www.youtube.com/user/californiacio"
                  target="_blank"
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: blue;
                      text-decoration: none;
                    "
                    ><img
                      border="0"
                      width="32"
                      height="32"
                      style="width: 0.3333in; height: 0.3333in"
                      id="_x0000_i1029"
                      src="cid:youtube_img"
                      alt="YouTube" /></span></a
                ><span
                  style="
                    font-size: 12pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  >&nbsp;</span
                ><a href="http://techblog.ca.gov/" target="_blank"
                  ><span
                    style="
                      font-size: 12pt;
                      font-family: 'Century Gothic', sans-serif;
                      color: blue;
                      text-decoration: none;
                    "
                    ><img
                      border="0"
                      width="32"
                      height="32"
                      style="width: 0.3333in; height: 0.3333in"
                      id="_x0000_i1030"
                      src="cid:blog_img"
                      alt="Blog" /></span></a
                ><span
                  style="
                    font-size: 9pt;
                    font-family: 'Century Gothic', sans-serif;
                  "
                  ><o:p></o:p
                ></span>
              </p>
            </td>
          </tr>
        </table>
        <p class="MsoNormal"><o:p>&nbsp;</o:p></p>
      </div>
    </body>
  </html>
  '''
