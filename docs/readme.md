
# Designing The Anonymised RA data store

# The anonymised DataInput

robodata --ano ----- handledperiods
         |        |
         |        --- <one for every model-type>
         |        |
         |        --- opensittings
         |        |
         |        --- <one sittings-period-file per sittings-period>
         |
         --anoindex-- guid2id
                   |
                   -- session to sitting
                   
# A Sitting

* a pupil
* a starttime
* an endtime
* a sequence of actions: time+actiontype+...
  . goto storylineitem
  . runscript
    . run-data
    . 
    . 
  . complete_storyline
  . complete_course
 
# calculating a new sittings-period
* start at the next period (from handledperiods)
* preload model-types
* preload opensittings