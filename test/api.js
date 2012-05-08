
bz = BugzillaTracker(url)

bz.search({ product: "css", component: "regions" }, callback)
bz.getUpdatedIssues(myIssues, serverIssues)

