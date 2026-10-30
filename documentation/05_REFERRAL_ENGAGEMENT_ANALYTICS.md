# Referral & Engagement Analytics Specification

## Referral lifecycle
Invite created/shared → invitee attributed → invitee registered → qualification conditions met → reward issued / expired / rejected.

## Required referral dimensions
referral_id, referrer_user_id, referred_user_id (nullable before registration), channel, created_at, attribution_timestamp, qualification_timestamp, status, campaign_id and reward reference.

## Engagement
Measure active users, session frequency, session duration (if meaningful), repeat task activity, feature adoption, notification delivery/open rates and retention.

## Attribution cautions
Define attribution windows, last-click/first-click rules, self-referral prevention, duplicate invite handling and fraud controls with product owners. Do not infer referral success from a link click alone.
