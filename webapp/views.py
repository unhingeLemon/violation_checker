from flask import Blueprint, render_template,jsonify,request, flash
from . import firebase_db

from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def violation_checker():
    if request.method == "POST":
        engineNumber = request.form.get('engineNumber')
        
        if(engineNumber != ''):

            car = None
            violations = []
            print("here")
            pushed_data = firebase_db.child("Cars").get()
            print(type(pushed_data))
            for i in pushed_data.each(): 
               
                if engineNumber == i.val()['engineNumber']:
                    key=i.key()
                    print("TRUE")
                    car = i.val()
                    
             

            if car != None:
                # car exist!

                # QUERY ITS VIOLATION:
                violation_query = firebase_db.child("Violations").get()
                print(violation_query)
                for i in violation_query.each():
                    print("inside")
                    print(type(i.val()["violationOwner"]))
                    if car["id"] == i.val()["violationOwner"]:
                        key=i.key()
                        # v = Violation(
                        #     violationName=i.val()["violationName"],
                        #     violationDesc=i.val()["violationDesc"],
                        #     violationOwner=i.val()["violationOwner"],
                        #     createdAt=i.val()["createdAt"],
                        #     isResolved=i.val()["isResolved"],
                        #     resolvedDate=i.val()["resolvedDate"],
                            
                        # )

                        v = i.val()
                        admins = firebase_db.child("Admin").get()
                        for a in admins.each(): 
                            if a.val()["id"] == v["violationAddedBy"]:
                                v["violationAddedBy"] = a.val()["name"]
                                v["adminContact"] = a.val()["adminContact"]

                 
                        violations.append(v)
                if(len(violations) <= 0):
                    flash("No Violations Found")
                return render_template("violationChecker.html",violations=violations, engineNumber=engineNumber, numViolation=len(violations))
            else:
                # Error handle if not exist
              
                flash("Engine Number Not Found")       






            return render_template("violationChecker.html", violations=violations, 
            engineNumber=engineNumber,
            numViolation=len(violations))

    return render_template("violationChecker.html")





