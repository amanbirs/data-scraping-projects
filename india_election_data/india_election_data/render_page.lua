

function main(splash)
	splash:go("http://www.indiavotes.com/ac/info?stateac=27&eid=176")
	splash:wait(0.5)
	local html = splash:html()
	return {html=html}
end