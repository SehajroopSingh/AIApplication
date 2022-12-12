import openai
from flask import Flask, request, render_template

# Set the GPT-3 API key and endpoint
openai.api_key = "YOUR_API_KEY"
openai.api_endpoint = "https://api.openai.com/v1/completions"

app = Flask(__name__)

@app.route("/")
def search_prompts():
    query = request.args.get("query")
    if query:
        # Use the `openai.Completion.create()` method to generate completions using GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=query,
            max_tokens=1024,
            n=5,
            temperature=0.5,
        )
        # Extract the generated completions from the response
        completions = [choice["text"] for choice in response["choices"]]
        return render_template("results.html", query=query, completions=completions)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run()
s




import OpenAI
import SwiftUI
import WatchKit

struct SearchView: View {
    @State var query = ""
    @State var isSearching = false
    @State var completions: [String] = []

    var body: some View {
        VStack {
            if !isSearching {
                // Show the search field and a button to start the search
                TextField("Enter a query", text: $query)
                Button("Search") {
                    // Start the search when the user taps the button
                    self.isSearching = true
                }
            } else {
                // Show the search results
                List(completions, id: \.self) { completion in
                    Text(completion)
                }
            }
        }
    }
}

class HostingController: WKHostingController<SearchView> {
    override var body: SearchView {
        let view = SearchView()

        // Set the GPT-3 API key and endpoint
        openai.api_key = "YOUR_API_KEY"
        openai.api_endpoint = "https://api.openai.com/v1/completions"

        view.isSearching = true
        // Use the `openai.Completion.create()` method to generate completions using GPT-3
        openai.Completion.create(
            engine="text-davinci-002",
            prompt=view.query,
            max_tokens=1024,
            n=5,
            temperature=0.5,
        ) { response, error in
            // Extract the generated completions from the response
            view.completions = response["choices"].map { $0["text"] }
        }

        return view
    }
}
