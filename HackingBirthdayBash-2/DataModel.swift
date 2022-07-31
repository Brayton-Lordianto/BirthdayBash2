//
//  DataModel.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import Foundation
import SwiftUI

class Gallery: ObservableObject {
    @Published var badges = [Badge]()
    
    init() {
        // load the badges
        self.loadBadges()
    }
    
    func loadBadges() {
        guard let url = URL(string: getBadgesLink) else{
            print("url not working")
            return
        }
        
        do {
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.addValue("application/json", forHTTPHeaderField: "Content-Type")
            request.addValue("application/json", forHTTPHeaderField: "Accept")
            
            // based on this, it seems to work
            let task = URLSession.shared.dataTask(with: request) {
                data, response, error in
                if (data == nil) { print("nil")}
                let s = try! JSONDecoder().decode([Badge].self, from: data!)
                self.badges = s
            }
            task.resume()
        }
    }
}

struct Badge: Identifiable, Codable {
    var id: String { imageURL.description }
    var imageURL: URL
    var date: String
    var hackathon: String
    var hackathonLink: URL
    var issuedBy: String
    var message: String
}

struct User: Codable {
    var name: String
    var devpostScreenName: String
    var devpostLink: URL {
        guard let link = URL(string: "https://devpost.com/\(devpostScreenName)") else {
            return URL(string: "https://www.google.com")!
        }
        return link
    }
}
