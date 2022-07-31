//
//  RequestFunctions.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import Foundation
import SwiftUI

let getBadgesLink  = "http://127.0.0.1:8000/get_badge_info"

func decodeBadgesData(userScreenName: String = "bl3321", badges: Binding<[Badge]>) {
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
            badges.wrappedValue = s
        }
        task.resume()
    }
}

func decodeBadgesData(userScreenName: String = "bl3321") -> [Badge] {
    guard let url = URL(string: getBadgesLink) else{ return [] }
    var badges = [Badge]()

    do {
//        let data = try? JSONEncoder().encode(data)
        
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
//        request.httpBody = data
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
        // based on this, it seems to work
        let task = URLSession.shared.dataTask(with: request) {
            data, response, error in
            if (data == nil) { print("nil")}
//            print(String(data: data!, encoding: .utf8)!)
            let s = try! JSONDecoder().decode([Badge].self, from: data!)
            badges = s
//            print(response ?? "no")
//            print(error ?? "none")
        }
        task.resume()
    }
    return badges
}

//func post(to urlString: String, _ data: [String:String]) {
//    guard let url = URL(string: urlString) else{return}
//
//    do {
//        let data = try? JSONEncoder().encode(data)
//
//
//        var request = URLRequest(url: url)
//        request.httpMethod = "POST"
//        request.httpBody = data
//        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
//        request.addValue("application/json", forHTTPHeaderField: "Accept")
//
//        // based on this, it seems to work
//        let task = URLSession.shared.dataTask(with: request) {
//            data, response, error in
//            if (data == nil) { print("nil")}
////            print(String(data: data!, encoding: .utf8)!)
//            print(try! JSONDecoder().decode([Badge].self, from: data!))
////            print(response ?? "no")
////            print(error ?? "none")
//        }
//        task.resume()
//    }
//
//}
//
//post(to: "http://127.0.0.1:8000/get_data", ["devpostScreenName":"bl3321"])
