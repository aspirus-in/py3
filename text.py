#!/bin/python3


class text:
	reset      = "\033[0m"
	r = reset
	bold       = "\033[1m"
	b = bold
	italic     = "\033[3m"
	i = italic
	underlined = "\033[4m"
	u = underlined
	blink      = "\033[5m"
	B = blink

	black   = "\033[30m"
	red     = "\033[31m"
	fgr = red
	green   = "\033[32m"
	fgg = green
	yellow  = "\033[33m"
	fgy =yellow
	blue    = "\033[34m"
	fgb = blue
	magenta = "\033[35m"
	fgm = magenta
	cyan    = "\033[36m"
	fgc = cyan
	white   = "\033[37m"
	
	brblack   = "\033[90m"
	brred     = "\033[91m"
	brr = brred
	brgreen   = "\033[92m"
	brg = brgreen
	bryellow  = "\033[93m"
	bry = bryellow
	brblue    = "\033[94m"
	brb = brblue
	brmagenta = "\033[95m"
	brm = brmagenta
	brcyan    = "\033[96m"
	brc = brcyan
	brwhite   = "\033[97m"

	bg_black   = "\033[40m"
	bg_red     = "\033[41m"
	bg_green   = "\033[42m"
	bg_yellow  = "\033[43m"
	bg_blue    = "\033[44m"
	bg_magenta = "\033[45m"
	bg_cyan    = "\033[46m"
	bg_white   = "\033[47m"
	
	bg_brblack   = "\033[100m"
	bg_brred     = "\033[101m"
	bg_brgreen   = "\033[102m"
	bg_bryellow  = "\033[103m"
	bg_brblue    = "\033[104m"
	bg_brmagenta = "\033[105m"
	bg_brcyan    = "\033[106m"
	bg_brwhite   = "\033[107m"


if __name__ == "__main__":
	print(f'''
{text.bold}[ bold ]{text.reset}
{text.italic}[ italic ]{text.reset}
{text.underlined}[ underlined ]{text.reset}
{text.blink}[ blink ]{text.reset}
{text.black       }[ black        ]{text.reset}
{text.red         }[ red          ]{text.reset}
{text.green       }[ green        ]{text.reset}
{text.yellow      }[ yellow       ]{text.reset}
{text.blue        }[ blue         ]{text.reset}
{text.magenta     }[ magenta      ]{text.reset}
{text.cyan        }[ cyan         ]{text.reset}
{text.white       }[ white        ]{text.reset}
{text.brblack     }[ brblack      ]{text.reset}
{text.brred       }[ brred        ]{text.reset}
{text.brgreen     }[ brgreen      ]{text.reset}
{text.bryellow    }[ bryellow     ]{text.reset}
{text.brblue      }[ brblue       ]{text.reset}
{text.brmagenta   }[ brmagenta    ]{text.reset}
{text.brcyan      }[ brcyan       ]{text.reset}
{text.brwhite     }[ brwhite      ]{text.reset}
{text.bg_black    }[ bg_black     ]{text.reset}
{text.bg_red      }[ bg_red       ]{text.reset}
{text.bg_green    }[ bg_green     ]{text.reset}
{text.bg_yellow   }[ bg_yellow    ]{text.reset}
{text.bg_blue     }[ bg_blue      ]{text.reset}
{text.bg_magenta  }[ bg_magenta   ]{text.reset}
{text.bg_cyan     }[ bg_cyan      ]{text.reset}
{text.bg_white    }[ bg_white     ]{text.reset}
{text.bg_brblack  }[ bg_brblack   ]{text.reset}
{text.bg_brred    }[ bg_brred     ]{text.reset}
{text.bg_brgreen  }[ bg_brgreen   ]{text.reset}
{text.bg_bryellow }[ bg_bryellow  ]{text.reset}
{text.bg_brblue   }[ bg_brblue    ]{text.reset}
{text.bg_brmagenta}[ bg_brmagenta ]{text.reset}
{text.bg_brcyan   }[ bg_brcyan    ]{text.reset}
{text.bg_brwhite  }[ bg_brwhite   ]{text.reset}
'''[1:-1])
