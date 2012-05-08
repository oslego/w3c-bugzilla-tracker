// Note: only publicly-accessible bugs (those not in any group) will be
// listed when using this JavaScript format. This is to prevent malicious
// sites stealing information about secure bugs.
  
bugs = new Array; 

  bugs[15679] = [ 
      "normal",
      "P2",
      "All",
      "alexmog",
      "NEW",
      "",
      "elementFromPoint and CSS regions"
  ];  
  bugs[16859] = [ 
      "normal",
      "P2",
      "All",
      "stearns",
      "NEW",
      "",
      "Reconsider using \x40rule for region styling"
  ];

if (window.buglistCallback) {
  buglistCallback(bugs);
}