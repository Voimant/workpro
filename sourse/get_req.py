def req_xml(gos, t_namber):
    req = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <soapenv:Header/>
   <soapenv:Body>
      <xs:RepairStatus>
         <xs:RequestJSONtext>{{"StateNumber": {gos},
    "VIN": NONE,
    "Phone": {t_namber}</xs:RequestJSONtext>
      </xs:RepairStatus>
   </soapenv:Body>
</soapenv:Envelope>"""
    return req
